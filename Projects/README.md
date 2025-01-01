# Projets
Bienvenue dans la section dédiée à mes projets en cybersécurité !  
Vous trouverez ici une variété de projets pratiques que j'ai réalisés pour renforcer mes compétences en sécurité des réseaux, des applications web, et des systèmes.

---

## 📋 Liste des Projets
- 🔍 **Conception et configuration d’un réseau sécurisé avec VLANs et routage dynamique (OSPF)**  
  - Création d’une architecture réseau simulée comprenant plusieurs VLANs pour segmenter le trafic.
  - Configuration des ports en mode access et trunk sur des switches, avec interconnexion via un routeur.
  - Mise en place du routage dynamique OSPF pour assurer la communication inter-VLAN et la redondance réseau.
  - Simulation et test de la topologie à l’aide de Cisco Packet Tracer.
  - 👉 [Consultez le projet ici](./OSPF_Network.md)

- 🌐 **Python : Network Scanner et Analyseur de Vulnérabilités**  
   - Développé un outil Python permettant de scanner un réseau et d’identifier les hôtes actifs, ports ouverts et services associés.
   - Intégré Nmap et Scapy pour détecter les vulnérabilités basées sur une base de données CVE.
   - Généré des rapports automatisés en formats CSV pour un usage pratique en audit de sécurité.
   - Technologies utilisées : Python, Scapy, Nmap, CSV.  
   - 👉 [Consultez le projet ici](./Python_Network_Scanner.md)

- 🔒 **Analyse et sécurisation contre une attaque DDoS ICMP**
  - Analyse d'une attaque par déni de service distribué (DDoS) utilisant une inondation de paquets ICMP, ayant causé une indisponibilité réseau.
  - Mise en œuvre de mesures de sécurité, y compris des règles de pare-feu pour limiter les paquets ICMP, et l'intégration d'un système IDS/IPS.
  - Création d'une checklist basée sur le cadre NIST CSF pour évaluer la posture de sécurité d'autres environnements.
  - Documentation d'un plan de réponse aux incidents et d'un plan de reprise d'activité (PRA) pour limiter l'impact des futures attaques.
  - 👉 **[Consultez le projet ici](./Security_Audit.md)**

- 🔍 **Analyse de vulnérabilités d’un serveur de base de données**  
  - Réalisation d’une évaluation des vulnérabilités d’un serveur MySQL dans un environnement Linux en suivant les directives du NIST SP 800-30.  
  - Identification des menaces potentielles (exfiltration de données, perturbation d’opérations critiques) et évaluation des risques (probabilité et 
   gravité).  
  - Mise en œuvre de recommandations : authentification forte, chiffrement TLS, contrôle d’accès basé sur les rôles, et liste blanche d’adresses IP.    
  - 👉 [Consultez le projet ici](./Vulnerability_Assessment_report.md)

 - **Analyseur de Trafic Réseau**
  - Description : Développé un outil Python utilisant la bibliothèque Scapy pour capturer, analyser et détecter les anomalies dans le trafic réseau.
  - Fonctionnalités principales :
    - Analyse des paquets en temps réel pour identifier les adresses IP source/destination, les protocoles utilisés, et la taille des paquets.
    - Détection des comportements suspects, comme les scans de ports ou les connexions répétées.
    - Génération de rapports détaillés en CSV pour une analyse approfondie.
  - - 👉 **[Consultez le projet ici](./Network_Traffic_Analyser.md)**