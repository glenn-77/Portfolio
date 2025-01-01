from scapy.all import sniff
import csv
from collections import Counter

# Fonction pour analyser chaque paquet capturé
def analyser_paquet(packet):
    if packet.haslayer("IP"):
        ip_src = packet["IP"].src
        ip_dst = packet["IP"].dst
        protocol = packet["IP"].proto
        size = len(packet)

        # Ajouter les informations capturées à une liste globale
        traffic_data.append({
            "source": ip_src,
            "destination": ip_dst,
            "protocol": protocol,
            "size": size
        })

# Fonction pour sauvegarder les résultats dans un fichier CSV
def sauvegarder_rapport(filename="traffic_report.csv"):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Source IP", "Destination IP", "Protocole", "Taille"])
        for data in traffic_data:
            writer.writerow([data["source"], data["destination"], data["protocol"], data["size"]])
    print(f"Rapport sauvegardé dans {filename}")

# Fonction pour détecter des anomalies simples
def detecter_anomalies():
    ip_counter = Counter([data["destination"] for data in traffic_data])
    for ip, count in ip_counter.items():
        if count > 50:  # Seuil d'anomalie (par exemple, plus de 50 connexions vers une IP)
            print(f"Anomalie détectée : {count} connexions vers l'IP {ip}")

# Liste pour stocker les données de trafic
traffic_data = []

# Capture de trafic réseau (5 secondes pour ce test)
print("Démarrage de la capture...")
sniff(prn=analyser_paquet, timeout=5)

# Analyse et détection d'anomalies
print("Analyse terminée. Détection des anomalies...")
detecter_anomalies()

# Sauvegarde des résultats dans un rapport CSV
sauvegarder_rapport()
