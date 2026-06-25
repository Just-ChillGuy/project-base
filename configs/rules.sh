#!/bin/bash

iptables -F

# VM1
iptables -A INPUT -p tcp -s 192.168.56.20 --dport 5432 -j ACCEPT
iptables -A INPUT -p tcp --dport 5432 -j DROP

# VM2
iptables -A INPUT -p tcp -s 192.168.56.40 --dport 8080 -j ACCEPT
iptables -A INPUT -p tcp --dport 8080 -j DROP

# VM3
iptables -A INPUT -p tcp -s 192.168.56.40 --dport 6379 -j ACCEPT
iptables -A INPUT -p tcp --dport 6379 -j DROP
