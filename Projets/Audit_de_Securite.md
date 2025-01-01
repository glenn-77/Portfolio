# Sécurisation Réseau : Analyse et Résolution d'une Attaque DDoS ICMP

Ce projet documente une analyse et une réponse détaillées à une attaque par déni de service distribué (DDoS) ciblant un réseau interne à l'aide d'un flux massif de paquets ICMP. Il s'appuie sur le cadre NIST Cybersecurity Framework (CSF) pour guider les étapes de sécurisation et inclut des contrôles spécifiques pour améliorer la posture de sécurité.

## Table des Matières
1. [Contexte](#contexte)
2. [Objectifs](#objectifs)
3. [Méthodologie](#méthodologie)
    - [Analyse de l'incident](#analyse-de-lincident)
    - [Plan d'action basé sur le NIST CSF](#plan-daction-basé-sur-le-nist-csf)
4. [Checklist de Sécurité](#checklist-de-sécurité)
5. [Recommandations](#recommandations)
6. [Ressources et Références](#ressources-et-références)

---

## Contexte

L'entreprise a subi une interruption des services réseau due à une attaque DDoS utilisant une inondation de paquets ICMP. Cette attaque a compromis le fonctionnement interne pendant deux heures avant d'être résolue.

### Résumé de l'incident
- **Type d'attaque** : DDoS par ICMP flooding
- **Impact** : Interruption de tous les services réseau internes
- **Réponse immédiate** : Blocage des paquets ICMP entrants et restauration des services critiques.

---

## Objectifs

1. Analyser l'attaque pour identifier les vulnérabilités exploitées.
2. Mettre en œuvre des mesures de protection robustes pour prévenir de futures attaques.
3. Documenter une checklist pour évaluer la sécurité d'autres environnements.
4. Utiliser le cadre NIST CSF pour une réponse méthodique.

---

## Méthodologie

### Analyse de l'incident

| **Fonction**       | **Action menée**                                                                                       |
|---------------------|-------------------------------------------------------------------------------------------------------|
| **Identify**        | L'attaque a ciblé le réseau interne via des paquets ICMP massifs non filtrés.                         |
| **Protect**         | Application de règles pare-feu pour limiter les paquets ICMP et mise en place d’un IDS/IPS.           |
| **Detect**          | Configuration du pare-feu pour vérifier les IP usurpées et surveillance réseau des flux anormaux.     |
| **Respond**         | Isolation des systèmes affectés et analyse des journaux réseau pour détecter les activités suspectes.|
| **Recover**         | Restauration des services critiques avant de réactiver les systèmes secondaires.                      |

---

### Plan d'action basé sur le NIST CSF

#### **1. Identifier**
- Réalisation d'un audit complet des actifs.
- Classification des données critiques (PII, SPII).
- Évaluation des vulnérabilités réseau.

#### **2. Protéger**
- Configuration stricte des pare-feu.
- Mise en place d'une politique de gestion des mots de passe.
- Sécurisation des données sensibles par chiffrement.

#### **3. Détecter**
- Déploiement d'outils IDS/IPS.
- Surveillance proactive avec analyse des journaux.

#### **4. Répondre**
- Documentation des processus de gestion des incidents.
- Simulation régulière d'incidents pour tester la résilience.

#### **5. Restaurer**
- Plan de reprise d’activité testé et documenté.
- Automatisation des restaurations critiques.

---

## Checklist de Sécurité

| **Contrôle**                          | **Statut** |
|---------------------------------------|------------|
| Pare-feu avec règles ICMP strictes    | ✅          |
| Vérification des IP usurpées          | ✅          |
| IDS/IPS en place                      | ✅          |
| Surveillance réseau proactive         | ✅          |
| Sauvegardes régulières des données    | ❌          |
| Gestion des mots de passe centralisée | ❌          |

---

## Recommandations

1. **Implémenter des sauvegardes** : Établir des politiques de sauvegarde régulières pour garantir la résilience.
2. **Renforcer la gestion des accès** : Implémenter le principe du moindre privilège pour limiter l'exposition.
3. **Sensibiliser les employés** : Formation sur les menaces et la réponse aux incidents.
4. **Évaluer régulièrement** : Effectuer des audits fréquents pour détecter les nouvelles vulnérabilités.

---

## Ressources et Références

1. NIST Cybersecurity Framework - [Applying the NIST CSF .pdf](https://github.com/user-attachments/files/18285944/Applying.the.NIST.CSF.pdf)
2. [Incident report analysis.pdf](https://github.com/user-attachments/files/18285959/Incident.report.analysis.pdf)
3. [Controls and compliance checklist.pdf](https://github.com/user-attachments/files/18285960/Controls.and.compliance.checklist.pdf)
4.[Botium Toys_ Scope, goals, and risk assessment report.pdf](https://github.com/user-attachments/files/18285942/Botium.Toys_.Scope.goals.and.risk.assessment.report.pdf)
