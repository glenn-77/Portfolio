# Network Vulnerability Scanner / Scanner de Vulnérabilités Réseau

## [🇫🇷 Version française](#scanner-de-vuln%C3%A9rabilit%C3%A9s-r%C3%A9seau)

# Network Vulnerability Scanner

## Introduction
This project is a **Python-based Network Vulnerability Scanner** designed to scan a target IP address, identify open ports, detect services and their versions, and analyze potential vulnerabilities using CVE (Common Vulnerabilities and Exposures) data. The scanner generates detailed reports in CSV and format, making it ideal for network security assessments.

---

## Features
- **Port Scanning**: Detect open ports on a target IP address using Python's `socket` library.
- **Advanced Scanning**: Leverage `nmap` to identify running services, versions, and perform vulnerability detection using Nmap's `vuln` scripts.
- **CVE Integration**: Search for known vulnerabilities using external CVE databases (via API).
- **Report Generation**:
  - CSV format for structured data.

---

## Prerequisites

### 1. Python Libraries
The following Python libraries are required:
- `socket`
- `nmap` (`python-nmap` package)
- `requests`
- `csv`


### 2. Tools
- **Nmap**: Ensure Nmap is installed on your system. You can download it [here](https://nmap.org/download.html).

---

## Installation
1. Clone this repository:
```bash
git clone https://github.com/yourusername/network-vulnerability-scanner.git
```
2. Navigate to the project directory:
```bash
cd network-vulnerability-scanner
```
3. Run the Python script:
```bash
python scanner.py
```

---

## Usage
1. Execute the script and input the target IP address when prompted.
2. The script performs the following steps:
   - Scans for open ports.
   - Uses Nmap to detect services and potential vulnerabilities.
   - Checks for CVEs associated with detected services.
3. Outputs the results in CSV file in the project directory.

### Example Output
- **CSV Report**: `scan_results.csv`
---

## Code Overview
### Key Functions
- `scanner_de_ports(ip, ports)`: Scans open ports using `socket`.
- `scan_avance(ip)`: Uses Nmap to detect services and potential vulnerabilities.
- `check_cve(service_name, version)`: Checks CVEs using the Vulners API.
- `save_to_csv(results, filename)`: Saves scan results in CSV format.

---

## Contribution
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature:
   ```bash
    git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
    git commit -m "Add your message here"
   ```
4. Push to your branch:
   ```bash
    git push origin feature-name
   ```
5. Open a pull request.

---

## Contact
For any questions or suggestions, feel free to contact me:
- GitHub: [glenn77](https://github.com/glenn77)

---

Thanks for your visit ! 🙌

---
# Scanner de Vulnérabilités Réseau

## Introduction
Ce projet est un **scanner de vulnérabilités réseau basé sur Python** conçu pour analyser une adresse IP cible, identifier les ports ouverts, détecter les services et leurs versions, et analyser les vulnérabilités potentielles en utilisant des données CVE (Common Vulnerabilities and Exposures). Le scanner génère des rapports détaillés aux formats CSV, ce qui le rend idéal pour des évaluations de la sécurité réseau.

---

## Fonctionnalités
- **Scan des ports** : Détecte les ports ouverts sur une adresse IP cible en utilisant la bibliothèque `socket` de Python.
- **Scan avancé** : Utilise `nmap` pour identifier les services en cours d'exécution, leurs versions et effectuer une détection des vulnérabilités à l'aide des scripts `vuln` de Nmap.
- **Intégration CVE** : Recherche des vulnérabilités connues en utilisant des bases de données CVE externes (via API).
- **Génération de rapports** :
  - Format CSV pour des données structurées.

---

## Prérequis

### 1. Bibliothèques Python
Les bibliothèques suivantes sont nécessaires :
- `socket`
- `nmap` (paquet `python-nmap`)
- `requests`
- `csv`

### 2. Outils
- **Nmap** : Assurez-vous que Nmap est installé sur votre système. Vous pouvez le télécharger [ici](https://nmap.org/download.html).

---

## Installation
1. Clonez ce dépôt :
```bash
git clone https://github.com/votrenomutilisateur/scanner-vulnerabilites-reseau.git
```
2. Accédez au répertoire du projet :
```bash
cd scanner-vulnerabilites-reseau
```
3. Exécutez le script Python :
```bash
python scanner.py
```

---

## Utilisation
1. Exécutez le script et saisissez l'adresse IP cible lorsqu'elle est demandée.
2. Le script effectue les étapes suivantes :
   - Analyse des ports ouverts.
   - Utilisation de Nmap pour détecter les services et vulnérabilités potentielles.
   - Recherche de CVE associées aux services détectés.
3. Générez les résultats sous forme de fichiers CSV dans le répertoire du projet.

### Exemple de sortie
- **Rapport CSV** : `scan_results.csv`

---

## Aperçu du Code
### Fonctions Clés
- `scanner_de_ports(ip, ports)` : Scanne les ports ouverts en utilisant `socket`.
- `scan_avance(ip)` : Utilise Nmap pour détecter les services et vulnérabilités potentielles.
- `check_cve(service_name, version)` : Recherche des CVE via l'API Vulners.
- `save_to_csv(results, filename)` : Sauvegarde les résultats dans un fichier CSV.

---

## Contribution
Les contributions sont les bienvenues ! Suivez ces étapes :
1. Forkez le dépôt.
2. Créez une nouvelle branche pour votre fonctionnalité :
   ```bash
    git checkout -b nom-de-la-fonctionnalite
   ```
3. Commitez vos modifications :
   ```bash
    git commit -m "Ajout d'une nouvelle fonctionnalité"
   ```
4. Poussez votre branche :
   ```bash
    git push origin nom-de-la-fonctionnalite
   ```
5. Ouvrez une pull request.

---

## 📬 Contact

Si vous avez des questions ou souhaitez discuter de ce projet, n’hésitez pas à me contacter via [mon profil GitHub](https://github.com/glenn77).

---

Merci de votre visite ! 🙌

