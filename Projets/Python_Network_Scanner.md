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

## Contact
Pour toute question ou suggestion, n'hésitez pas à me contacter :
- Email : [votre-email@example.com](mailto:votre-email@example.com)
- GitHub : [votrenomutilisateur](https://github.com/votrenomutilisateur)

