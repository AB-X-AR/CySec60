import requests

#OWASP SECURITY HEADER

weakheaders = {
    "Strict-Transport-Security": lambda v: not v or "max-age" not in v.lower(),
    "Content-Security-Policy": lambda v: not v or "*" in v,
    "X-Frame-Options": lambda v: not v or "allow-from" in v.lower(),
    "X-Content-Type-Options": lambda v: v.lower() != "nosniff",
    "Referrer-Policy": lambda v: not v or "unsafe-url" in v.lower(),
    "Permissions-Policy": lambda v: not v or "*" in v,
    "Cross-Origin-Resource-Policy": lambda v: not v or "cross-origin" in v.lower(),
    "Cross-Origin-Opener-Policy": lambda v: not v,
    "Cross-Origin-Embedder-Policy": lambda v: not v
}
url = input("Enter website url : ")

if not url.startswith(("http://", "https://")): # We check url has scheme if no add http
    url = "http://" + url

try:
    response = requests.get(url, timeout=10)
    headers = response.headers
    print("---HTTP HEADER ANALYZER---")
    print(f"---TARGET : {url} -------")
    print("--------------------------")
    for header, check in weakheaders.items():
        value = headers.get(header, "")
        if check(value):
            print(f"[WEAK] {header} - {value or 'Missing'}")
        else:
            print(f"[GOOD] {header} - {value}")

except Exception as e:
    print("Error:",e)

