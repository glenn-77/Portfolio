from scapy.all import sniff
import csv
from collections import Counter

# Function to analyze each captured packet
def analyze_paquet(packet):
    if packet.haslayer("IP"):
        ip_src = packet["IP"].src
        ip_dst = packet["IP"].dst
        protocol = packet["IP"].proto
        size = len(packet)

        # Add captured information to a global list
        traffic_data.append({
            "source": ip_src,
            "destination": ip_dst,
            "protocol": protocol,
            "size": size
        })

# Function to save results in a CSV file
def save_report(filename="traffic_report.csv"):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["IP Source", "IP Destination ", "Protocol", "Size"])
        for data in traffic_data:
            writer.writerow([data["source"], data["destination"], data["protocol"], data["size"]])
    print(f"Report saved in {filename}")

# Function to detect simple anomalies
def detect_anomalies():
    ip_counter = Counter([data["destination"] for data in traffic_data])
    for ip, count in ip_counter.items():
        if count > 50:  # Anomaly thresold (for example, more of 50 connections to a IP address)
            print(f"Anomaly detected : {count} connections to IP {ip}")

# List to stock traffic data
traffic_data = []

# Traffic network capture (5 seconds for this test)
print("Beginning of the capture...")
sniff(prn=analyze_paquet, timeout=5)

# Analyze and detection of anomalies
print("Analyze done. Detection of anomalies...")
detect_anomalies()

# Save of results in a CSV report
save_report()
