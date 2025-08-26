# HTTP Header Analyzer - Day 1

A Python script that fetches a website’s HTTP response headers, checks for weak security headers like Content-Security-Policy and Strict-Transport-Security, and fingerprints the server technology. Useful for quick reconnaissance and spotting basic misconfigurations. Finally returns GOOD and WEAK Headers.

So what are the Security Header?
Security headers are directives used by web applications to configure security defenses in web browsers. Based on these directives, browsers can make it harder to exploit client-side vulnerabilities such as Cross-Site Scripting or Clickjacking. [acc-to-GOOGLE].

## Reference
I built this project based on **OWASP** [CHEATSHEET](https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Headers_Cheat_Sheet.html).

## Features
- Fetches HTTP response headers
- Flags missing or weak configurations


## Usage

1. Copy RAW or Download the Python program.

```bash
> pip3 install requests
#Requests - Makes the HTTP request and retrieves headers.
> python3 http-header-analyer.py
```
### Result
```bash
Enter website url : cloudflare.com
---HTTP HEADER ANALYZER---
---TARGET : http://cloudflare.com -------
--------------------------
[GOOD] Strict-Transport-Security - max-age=31536000; includeSubDomains
[WEAK] Content-Security-Policy - Missing
[GOOD] X-Frame-Options - SAMEORIGIN
[GOOD] X-Content-Type-Options - nosniff
[GOOD] Referrer-Policy - strict-origin-when-cross-origin
[GOOD] Permissions-Policy - geolocation=(), camera=(), microphone=()
[WEAK] Cross-Origin-Resource-Policy - Missing
[WEAK] Cross-Origin-Opener-Policy - Missing
[WEAK] Cross-Origin-Embedder-Policy - Missing
```

## DROP A STAR AND KICKSTART WITH ME WITH FORK

---

<p align="center">
  <a href="https://github.com/AB-X-AR/WebSec60/stargazers">
    <img src="https://img.shields.io/github/stars/AB-X-AR/WebSec60?style=for-the-badge" alt="GitHub stars">
  </a>
  <a href="https://github.com/AB-X-AR/WebSec60/network/members">
    <img src="https://img.shields.io/github/forks/AB-X-AR/WebSec60?style=for-the-badge" alt="GitHub forks">
  </a>
  <img src="https://img.shields.io/badge/python-3.8%2B-blue?style=for-the-badge" alt="Python version">
</p>

---
