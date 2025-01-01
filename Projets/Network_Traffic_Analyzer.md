# Network Traffic Analyzer / Analyseur de Trafic Réseau

## [🇫🇷 Version française](#analyseur-de-trafic-r%C3%A9seau)

## Description

The **Network Traffic Analyzer** is a Python-based tool using the Scapy library. It captures and analyzes network packets in real-time to:
- Identify source and destination IP addresses.
- Extract used protocols.
- Detect anomalies in network traffic (e.g., an unusual number of connections).
- Generate a detailed report of captured data in CSV format.

---

## Features

1. **Real-time capture:** Captures network packets on the local interface.
2. **Packet analysis:** Identifies IP addresses, protocols, and packet sizes.
3. **Anomaly detection:** Highlights suspicious behavior (e.g., port scans).
4. **Analysis report:** Saves the results in a CSV file.

---

## Prerequisites

- Python 3.6 or later
- Python libraries:
  - `scapy`
  - `csv`
- Administrative privileges (to capture network traffic)

---

## Installation
- [mon_script.py](./traffic_analyser.py) : Script Python
1. Clone this repository:
```bash
git clone https://github.com/your-repo/network-traffic-analyzer.git
```
2. Install dependencies:
```bash
pip install scapy
```

---

## Usage

1. Run the Python script:
```bash
sudo python3 traffic_analyzer.py
```
2. The program captures traffic for 5 seconds by default, analyzes packets, detects anomalies, and generates a CSV report.

---

## Example Output

```
Starting capture...
Analysis complete. Detecting anomalies...
Anomaly detected: 60 connections to IP 192.168.1.100
Report saved to traffic_report.csv
```

---

## Contact
If you have questions or if you want to talk about the project, don't hesitate to contact me at my profile [mon profil GitHub](https://github.com/glenn77).

---

Thanks for your visit ! 🙌

---

# Analyseur de Trafic Réseau

## Description

L'**Analyseur de Trafic Réseau** est un outil basé sur Python utilisant la bibliothèque Scapy. Il permet de capturer et d'analyser les paquets réseau en temps réel pour :
- Identifier les adresses IP source et destination.
- Extraire les protocoles utilisés.
- Détecter des anomalies dans le trafic réseau (par exemple, un nombre inhabituel de connexions).
- Générer un rapport détaillé des données capturées au format CSV.

---

## Fonctionnalités

1. **Capture en temps réel :** Capture les paquets réseau sur l'interface locale.
2. **Analyse des paquets :** Identifie les adresses IP, protocoles et tailles des paquets.
3. **Détection d'anomalies :** Met en évidence des comportements suspects (exemple : scans de ports).
4. **Rapport d'analyse :** Sauvegarde les résultats dans un fichier CSV.

---

## Prérequis

- Python 3.6 ou plus récent
- Bibliothèques Python :
  - `scapy`
  - `csv`
- Droits administratifs (pour capturer le trafic réseau)

---

## Installation
- [mon_script.py](./traffic_analyser.py) : Script Python
1. Clonez ce dépôt :
```bash
git clone https://github.com/votre-repo/analyseur-trafic-reseau.git
```
2. Installez les dépendances :
```bash
pip install scapy
```

---

## Utilisation

1. Lancez le script Python :
```bash
sudo python3 traffic_analyzer.py
```
2. Le programme capture le trafic pendant 5 secondes par défaut, analyse les paquets, détecte les anomalies et génère un rapport CSV.

---

## Exemple de sortie

```
Démarrage de la capture...
Analyse terminée. Détection des anomalies...
Anomalie détectée : 60 connexions vers l'IP 192.168.1.100
Rapport sauvegardé dans traffic_report.csv
```

---
## 📬 Contact

Si vous avez des questions ou souhaitez discuter de ce projet, n’hésitez pas à me contacter via [mon profil GitHub](https://github.com/glenn77).

---

Merci de votre visite ! 🙌


