import requests
import argparse
import os

#Commands
parser = argparse.ArgumentParser(description="DIRECTORY BRUTE forcer")
parser.add_argument("-u", "--url", required=True, help="Target url")
parser.add_argument("-w", "--wordlist", required=True, help="Wordlist Path")
args = parser.parse_args()

#Check wordlist existence
if not os.path.exists(args.wordlist):
    print(f"Error: Wordlist file '{args.wordlist}' not found.")
    exit(1)

# Load wordlist
with open(args.wordlist, "r") as file:
    paths = [line.strip() for line in file if line.strip()]

print(f"\nScanning {args.url} for directories...\n")


for path in paths:
    url = f"{args.url.rstrip('/')}/{path}"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"[200 OK] Found: {url}")
        else:
            print(f"[{response.status_code}] {url}")
    except requests.RequestException:
        print(f"Could not reach: {url}")
