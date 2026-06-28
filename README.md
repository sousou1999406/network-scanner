<img width="382" height="140" alt="image" src="https://github.com/user-attachments/assets/e5fc3ce3-0da9-42ce-8f04-03147e6f5568" />


# 🔍 Network Port Scanner

> A Python-based cybersecurity tool for network reconnaissance and port scanning.

## 🎯 What It Does
- Scans any target IP or domain for open ports
- Identifies running services (FTP, SSH, HTTP, HTTPS, MySQL...)
- Generates an automatic scan report saved as `.txt`
- Built with Python using only built-in libraries

## 🛠️ Tools & Technologies
- Python 3
- Socket library
- Datetime module

## 🚀 How To Run
```bash
py scanner.py
```
Then enter:
- Target: `scanme.nmap.org` or any IP
- Start port: `1`
- End port: `1000`

## 📊 Example Output
```--------------------------------------------------
Scanning Target: scanme.nmap.org
Time: 2026-06-28 17:38:31
--------------------------------------------------
[OPEN] Port 21 --> FTP
[OPEN] Port 22 --> SSH
[OPEN] Port 80 --> HTTP
--------------------------------------------------
Scan Complete! 3 open ports found
Report saved: scan_report.txt
```
## ⚠️ Disclaimer
This tool is for **educational purposes only**.  
Only scan systems you have permission to test.

## 👩‍💻 Author
**Soukaina Douazi** — Cybersecurity Student | SOC Analyst in Training  
📍 Casablanca, Morocco  
🔗 [LinkedIn](https://linkedin.com/in/soukaina-douazi)
