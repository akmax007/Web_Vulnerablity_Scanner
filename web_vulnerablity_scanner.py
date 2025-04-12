import requests
from bs4 import BeautifulSoup

def check_clickjacking(url):
    try:
        result = requests.get(url)
        if 'X-Frame-Options' not in result.headers:
            print("[Clickjacking] 🔴 Vulnerable - No X-Frame-Options header")
        else:
            print(f"[Clickjacking] 🟢 Protected - X-Frame-Options: {result.headers['X-Frame-Options']}")
    except Exception as e:
        print(f"[Clickjacking] ❌ Error: {e}")

def check_xss(url):
    try:
        xss_payload = "<script>alert('XSS')</script>"
        test_url = url + "?test=" + xss_payload
        result = requests.get(test_url)
        if xss_payload in result.text:
            print("[XSS] 🔴 Vulnerable - Payload reflected in response")
        else:
            print("[XSS] 🟢 Not vulnerable - Payload not reflected")
    except Exception as e:
        print(f"[XSS] ❌ Error: {e}")

def check_sql_injection(url):
    try:
        sqlinjection_payload = "' OR '1'='1"
        test_url = url + "?id=" + sqlinjection_payload
        result = requests.get(test_url)
        if any(error in result.text.lower() for error in ["sql syntax", "mysql", "oracle", "sqlite", "you have an error"]):
            print("[SQL Injection] 🔴 Potentially vulnerable - SQL error in response")
        else:
            print("[SQL Injection] 🟢 Not vulnerable - No SQL error detected")
    except Exception as e:
        print(f"[SQL Injection] ❌ Error: {e}")

def scan(url):
    print("\n--- Scanning URL:", url, "---\n")
    check_clickjacking(url)
    check_xss(url)
    check_sql_injection(url)
    print("\n--- Scan Complete ---")

if __name__ == "__main__":
    target_url = input("Enter the target URL (e.g. http://example.com/page): ").strip()
    scan(target_url)
