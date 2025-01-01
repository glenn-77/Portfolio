#!/bin/bash

# Firewall configuration script using iptables
# Tested on Debian/Ubuntu-based Linux distributions
# Run as root or with sudo

echo "Configuring the firewall..."

# Variables
IPTABLES=/sbin/iptables
LOOPBACK="127.0.0.1"

# Reset existing rules
$IPTABLES -F
$IPTABLES -X
$IPTABLES -t nat -F
$IPTABLES -t nat -X
$IPTABLES -t mangle -F
$IPTABLES -t mangle -X

# Default policy: block all traffic
$IPTABLES -P INPUT DROP
$IPTABLES -P OUTPUT DROP
$IPTABLES -P FORWARD DROP

# Allow loopback (localhost) traffic
$IPTABLES -A INPUT -i lo -j ACCEPT
$IPTABLES -A OUTPUT -o lo -j ACCEPT

# Allow established and related connections
$IPTABLES -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
$IPTABLES -A OUTPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

# Allow SSH (default port 22, adjust if needed)
SSH_PORT=22
$IPTABLES -A INPUT -p tcp --dport $SSH_PORT -m conntrack --ctstate NEW -j ACCEPT
$IPTABLES -A OUTPUT -p tcp --sport $SSH_PORT -j ACCEPT

# Allow HTTP (port 80) and HTTPS (port 443)
$IPTABLES -A INPUT -p tcp -m multiport --dports 80,443 -m conntrack --ctstate NEW -j ACCEPT
$IPTABLES -A OUTPUT -p tcp -m multiport --sports 80,443 -j ACCEPT

# Allow ping (ICMP)
$IPTABLES -A INPUT -p icmp --icmp-type echo-request -j ACCEPT
$IPTABLES -A OUTPUT -p icmp --icmp-type echo-reply -j ACCEPT

# Block all other ICMP traffic to prevent abuse
$IPTABLES -A INPUT -p icmp -j DROP
$IPTABLES -A OUTPUT -p icmp -j DROP

# Log denied packets
$IPTABLES -A INPUT -j LOG --log-prefix "iptables INPUT denied: " --log-level 4
$IPTABLES -A FORWARD -j LOG --log-prefix "iptables FORWARD denied: " --log-level 4
$IPTABLES -A OUTPUT -j LOG --log-prefix "iptables OUTPUT denied: " --log-level 4

# Save rules (specific to Debian/Ubuntu)
if [ -x /sbin/iptables-save ]; then
    iptables-save > /etc/iptables/rules.v4
    echo "Firewall rules saved in /etc/iptables/rules.v4"
fi

echo "Firewall configuration complete."
