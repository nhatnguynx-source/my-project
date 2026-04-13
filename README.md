# 🛡️ Cybersecurity & Python Portfolio
Chào mừng bạn đến với kho lưu trữ dự án của tôi. Đây là nơi tập trung các dự án về bảo mật hệ thống và lập trình Python.

---

## 🏗️ 1. Dự án: Vulnerability Assessment & Exploitation (Kioptrix Level 1)
Dự án thực hiện quy trình Pentest toàn diện trên môi trường máy chủ giả lập để chiếm quyền điều khiển tối cao (Root).

* **Công nghệ:** Kali Linux, Nmap, Metasploit, Wireshark.
* **Các lỗ hổng đã xác định:**
    * **Samba 2.2.1a (trans2open):** Khai thác lỗ hổng Buffer Overflow để chiếm Root shell thành công.
    * **SSL/TLS Vulnerabilities:** Phát hiện các lỗi bảo mật nghiêm trọng (POODLE, CCS Injection, Weak DH Group) qua quét Nmap Scripting Engine (NSE).
* **Tài liệu:**
    * 📄 [Báo cáo Vulnerability Assessment & Exploitation (Google Docs)](https://docs.google.com/document/d/10JX6g9oxGI9HIPWLpTfJ2Td8I0B84qns/edit)

---

## 🏨 2. Dự án: Smart Hotel Booking System (Python Security Focus)
Ứng dụng quản lý đặt phòng khách sạn được xây dựng bằng lập trình hướng đối tượng (OOP), tập trung vào các cơ chế xác thực an toàn.

* **Tính năng chính:**
    * **Quản lý phòng (OOP):** Sử dụng các Class `User` và `Room` để quản lý trạng thái đặt phòng và thông tin người dùng.
    * **Cơ chế Bảo mật (Security Alert):** Tự động phát hiện hành vi Brute-force; hệ thống sẽ tự động khóa (Lockdown) trong 60 giây nếu nhập sai mật khẩu quá 3 lần.
    * **Xử lý logic:** Kiểm tra độ dài mật khẩu (min 6 chars) và xác thực tài khoản thời gian thực.
* **Mã nguồn & Tài liệu:**
    * 💻 [Xem tài liệu Hotel Booking tại đây](./Hotel%20booking.py)
    * 📄 [Báo cáo dự án Smart Hotel Booking System (Google Docs)](https://docs.google.com/document/d/1rb_eC6TBOM6L9ibrzeYwLkfvw61cJyBaXHNmmqNbvuI/edit?tab=t.0#heading=h.7vdakvu8km9u)

---

## 🛠️ Kỹ năng kỹ thuật (Tech Stack)
* **Pentesting:** Network Discovery (Nmap), Vulnerability Scanning, Metasploit Framework.
* **Traffic Analysis:** Deep Packet Inspection với Wireshark.
* **Programming:** Python OOP, Security Logic (Rate Limiting/Lockout mechanism).

---

## 📬 Liên hệ
* **Email:** anhnhatn026@gmail.com
* **GitHub:** [anhnhatn026-beep](https://github.com/anhnhatn026-beep)


---
*Cảm ơn bạn đã ghé thăm repository của mình!*
