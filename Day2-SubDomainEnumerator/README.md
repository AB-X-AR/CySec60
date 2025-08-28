# Subdomain Enumerator

A simple Bash script to find valid subdomains for a given domain using DNS lookups and HTTP status checks.

## Features
- Reads subdomains from a wordlist
- Resolves DNS using `dig`
- Checks for HTTP 200 OK responses

## Requirements
- Bash
- dig (DNS utility)
- curl

## Usage
1. Add subdomains to `subdomains.txt` , you can also edit the file name.
2. Run the script:

```bash
./subenum.sh example.com
