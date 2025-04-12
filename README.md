# 🛡️ Web Vulnerability Scanner (Python)

A lightweight Python-based tool to detect common web vulnerabilities:

- 🔍 **Clickjacking**
- ⚔️ **Cross-Site Scripting (XSS)**
- 🛠️ **SQL Injection**

This scanner is designed for basic security testing and educational use. Ideal for beginners learning about web security concepts.

---

## ⚠️ Disclaimer

> This tool is intended **only for authorized testing and educational purposes**.  
> **Do not scan any website without explicit permission. Unauthorized scanning is illegal.**

---

## 🚀 Features

- ✅ Checks for missing `X-Frame-Options` header (Clickjacking)
- ✅ Basic XSS payload injection and reflection detection
- ✅ SQL Injection detection using error-based patterns
- 🧾 Clean console output with vulnerability status

---

## 🛠️ Setup

Install required dependencies:

```bash
  pip install requests beautifulsoup4
```
## ▶️ How to Use:
    python scanner.py
  Then enter the target URL when prompted:
    
    Enter the target URL (e.g. http://example.com/page): http://testphp.vulnweb.com/listproducts.php?cat=1
## 📤 Sample Output:

    --- Scanning URL: http://testphp.vulnweb.com/listproducts.php ---
    
    [Clickjacking] 🔴 Vulnerable - No X-Frame-Options header
    [XSS] 🔴 Vulnerable - Payload reflected in response
    [SQL Injection] 🔴 Potentially vulnerable - SQL error in response
    
    --- Scan Completed ---
