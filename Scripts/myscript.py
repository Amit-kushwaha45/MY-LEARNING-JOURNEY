#!/bin/bash

echo "Enter your first IP:"
read first_ip

echo "Enter last octet number:"
read last_octet

echo "Enter port no:"
read port

# Nmap scan and save results
proxychains nmap -sT $first_ip-$last_octet -p $port -oG mysqlscan > /dev/null

# Filter open ports
cat mysqlscan | grep open > mysqlscan2

echo "Scan complete. Check mysqlscan2 for results."  
