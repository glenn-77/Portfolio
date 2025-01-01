# Rapport d'Évaluation de Vulnérabilités

## Présentation du Projet
Ce dépôt contient les résultats et la méthodologie d'une évaluation de vulnérabilités réalisée sur un serveur de base de données. L'évaluation a été menée conformément aux lignes directrices du **NIST SP 800-30 Rev. 1**, garantissant une approche méthodique et professionnelle de l'analyse des risques et des stratégies de remédiation.

L'objectif principal de cette évaluation était d'identifier les vulnérabilités potentielles, d'évaluer les risques associés et de proposer des stratégies de remédiation concrètes pour améliorer la sécurité du système.

---

## Description du Système
- **Matériel** : Processeur haute performance avec 128 Go de RAM.
- **Système d'exploitation** : Dernière distribution Linux.
- **Système de gestion de bases de données (SGBD)** : MySQL.
- **Configuration réseau** : IPv4 avec connexions chiffrées SSL/TLS.
- **Utilisation** : Stockage et gestion des données clients, campagnes et analyses pour les opérations marketing.

---

## Portée de l'Évaluation
L'évaluation s'est concentrée sur les **contrôles d'accès** du serveur de base de données pendant une période de trois mois. Elle comprenait :
- L'évaluation de l'authentification et de l'autorisation des utilisateurs.
- L'analyse de la sécurité des transmissions de données.
- L'identification des permissions d'accès ouvertes et des risques potentiels.

---

## Méthodologie
L'évaluation a été réalisée conformément au **NIST SP 800-30 Rev. 1**, incluant les étapes suivantes :

1. **Identification des sources de menaces** :
   - Externes : Hackers, concurrents.
   - Internes : Employés, clients.

2. **Événements de menace** :
   - Exfiltration de données.
   - Perturbation des opérations.
   - Modification non autorisée des données critiques.

3. **Analyse des risques** :
   - Probabilité des événements de menace.
   - Gravité des impacts potentiels.
   - Calcul des scores de risque.

4. **Stratégies de remédiation** :
   - Mots de passe forts et authentification multi-facteurs.
   - Contrôle d'accès basé sur les rôles (RBAC).
   - Liste blanche d'adresses IP pour les accès réseau.
   - Migration de SSL vers TLS pour sécuriser les transmissions de données.

---

## Résultats Clés
| Source de Menace | Événement de Menace                    | Probabilité | Gravité | Risque |
|-------------------|---------------------------------------|-------------|---------|--------|
| Hacker            | Exfiltration de données               | 3           | 3       | 9      |
| Employé           | Perturbation des tâches critiques     | 2           | 3       | 6      |
| Client            | Modification non autorisée des données | 1           | 3       | 3      |

---

## Recommandations
Les actions suivantes ont été proposées pour traiter les risques identifiés :

- **Authentification** : Appliquer des politiques de mots de passe forts et mettre en place l'authentification multi-facteurs.
- **Autorisation** : Implémenter un RBAC pour limiter les privilèges des utilisateurs.
- **Sécurité des données** : Chiffrer toutes les données en mouvement avec TLS.
- **Restrictions réseau** : Restreindre l'accès au serveur via une liste blanche d'adresses IP.

---

## Comment Utiliser ce Dépôt
1. **Documentation** : Le fichier `Rapport_Evaluation_Vulnerabilites.docx` fournit des informations détaillées sur l'évaluation.
   - [NIST SP 800-30 Rev. 1.pdf](https://github.com/user-attachments/files/18285874/NIST.SP.800-30.Rev.1.pdf)
2. **Références Méthodologiques** : Consultez `NIST_SP_800-30.pdf` pour le cadre théorique guidant l'évaluation.
   - [Vulnerability assessment report exemplar.docx](https://github.com/user-attachments/files/18285872/Vulnerability.assessment.report.exemplar.docx)
