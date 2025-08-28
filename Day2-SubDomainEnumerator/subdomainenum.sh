!#/bin/bash

#Input
if [ -z "$1" ]; then
    echo "Usage : $0 <domain>"
    exit 1
fi
domain=$1
wordlist="subdomains.txt"

echo "Scanning subdomains for Target : $domain"
echo "----------------------------------------"

while read sub; do
    fqdn="$sub.$domain"
    ip=$(dig +short "$fqdn")

    if [ -n "$ip" ]; then
        # Try HTTP request
        response=$(curl -s -o /dev/null -w "%{http_code}" "http://$fqdn")

        if [ "$response" == "200" ]; then
            echo "[200 OK] $fqdn ($ip)"
        else
            echo "[$response] $fqdn ($ip)"
        fi
    fi
done < "$wordlist"