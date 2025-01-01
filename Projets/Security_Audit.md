# Network Security: Analysis and Resolution of an ICMP DDoS Attack

## [Lire la version française](#version-française)

This project documents a detailed analysis and response to a distributed denial-of-service (DDoS) attack targeting an internal network using a massive flow of ICMP packets. It is based on the NIST Cybersecurity Framework (CSF) to guide the steps for securing the network and includes specific controls to enhance security posture.

## Table of Contents
1. [Context](#context)
2. [Objectives](#objectives)
3. [Methodology](#methodology)
    - [Incident Analysis](#incident-analysis)
    - [Action Plan Based on NIST CSF](#action-plan-based-on-nist-csf)
4. [Security Checklist](#security-checklist)
5. [Recommendations](#recommendations)
6. [Resources and References](#resources-and-references)

---

## Context

The company experienced a network service disruption caused by a DDoS attack using an ICMP flood. This attack compromised internal operations for two hours before being resolved.

### Incident Summary
- **Type of Attack**: ICMP flooding DDoS
- **Impact**: Disruption of all internal network services
- **Immediate Response**: Blocked incoming ICMP packets and restored critical services.

---

## Objectives

1. Analyze the attack to identify exploited vulnerabilities.
2. Implement robust protection measures to prevent future attacks.
3. Document a checklist to evaluate the security of other environments.
4. Use the NIST CSF framework for a systematic response.

---

## Methodology

### Incident Analysis

| **Function**       | **Action Taken**                                                                                       |
|---------------------|-------------------------------------------------------------------------------------------------------|
| **Identify**        | The attack targeted the internal network through unfiltered massive ICMP packets.                     |
| **Protect**         | Applied firewall rules to limit ICMP packets and implemented IDS/IPS.                                 |
| **Detect**          | Configured firewall to check for spoofed IPs and monitored anomalous network flows.                   |
| **Respond**         | Isolated affected systems and analyzed network logs for suspicious activity.                          |
| **Recover**         | Restored critical services before reactivating secondary systems.                                     |

---

### Action Plan Based on NIST CSF

#### **1. Identify**
- Conducted a comprehensive asset audit.
- Classified critical data (PII, SPII).
- Assessed network vulnerabilities.

#### **2. Protect**
- Enforced strict firewall configurations.
- Implemented a password management policy.
- Secured sensitive data through encryption.

#### **3. Detect**
- Deployed IDS/IPS tools.
- Proactively monitored logs for analysis.

#### **4. Respond**
- Documented incident management processes.
- Regularly simulated incidents to test resilience.

#### **5. Recover**
- Tested and documented disaster recovery plans.
- Automated critical restoration processes.

---

## Security Checklist

| **Control**                          | **Status** |
|---------------------------------------|------------|
| Firewall with strict ICMP rules       | ✅          |
| Spoofed IP verification               | ✅          |
| IDS/IPS in place                      | ✅          |
| Proactive network monitoring          | ✅          |
| Regular data backups                  | ❌          |
| Centralized password management       | ❌          |

---

## Recommendations

1. **Implement Backups**: Establish regular backup policies to ensure resilience.
2. **Enhance Access Management**: Implement least privilege principles to minimize exposure.
3. **Employee Awareness**: Train staff on threats and incident response.
4. **Regular Evaluations**: Perform frequent audits to detect new vulnerabilities.

---

## Resources and References

1. NIST Cybersecurity Framework - [Applying the NIST CSF .pdf](https://github.com/user-attachments/files/18285944/Applying.the.NIST.CSF.pdf)
2. [Incident report analysis.pdf](https://github.com/user-attachments/files/18285959/Incident.report.analysis.pdf)
3. [Controls and compliance checklist.pdf](https://github.com/user-attachments/files/18285960/Controls.and.compliance.checklist.pdf)
- [Botium Toys_ Scope, goals, and risk assessment report.pdf](https://github.com/userattachments/files/18285942/Botium.Toys_.Scope.goals.and.risk.assessment.report.pdf)

## 📬 Contact

If you have any questions or want to discuss this project, feel free to contact me via [my GitHub profile](https://github.com/glenn77).

---

# Version Française

## Sécurisation Réseau : Analyse et Résolution d'une Attaque DDoS ICMP

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
- [Botium Toys_ Scope, goals, and risk assessment report.pdf](https://github.com/userattachments/files/18285942/Botium.Toys_.Scope.goals.and.risk.assessment.report.pdf)

## 📬 Contact

Si vous avez des questions ou souhaitez discuter de ce projet, n’hésitez pas à me contacter via [mon profil GitHub](https://github.com/glenn77).

---
