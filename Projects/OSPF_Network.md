# Design and Configuration of a Secure Network with VLANs and Dynamic Routing (OSPF)

## [🇫🇷 Version française ici](#version-française)

This project showcases the design and configuration of a secure network using VLANs for traffic segmentation and dynamic routing with OSPF to enable efficient and scalable communication between sub-networks.

## 🚀 Project Objectives

1. **Segment the local network (LAN)** to improve security and traffic management using VLANs.
2. **Configure dynamic routing with OSPF** to enable communication between VLANs.
3. **Test connectivity and network security** using simulation tools.

## 🛠️ Tools and Technologies Used

- **Cisco Packet Tracer**: Network simulation and configuration.
- **Network Protocols**: VLANs (802.1Q), OSPF (Open Shortest Path First).
- **Simulated Hardware**: Switches, routers, and PCs.

## 📖 Steps to Achieve the Project

### 1. **VLAN Configuration**
   - VLAN 10: IT Department.
   - VLAN 20: Marketing Department.
   - VLAN 30 : RH Department.
   - VLAN 40 : Business Department.
   - Configured ports in **access mode** for end devices and **trunk mode** for interconnection between network devices.

### 2. **Inter-VLAN Configuration**
   - Configured router sub-interfaces:
     - `192.168.10.1/24` for VLAN 10.
     - `192.168.20.1/24` for VLAN 20.
     - `192.168.30.1/24` for VLAN 30.
     - `192.168.40.1/24` for VLAN 40.


### 3. **Dynamic Routing with OSPF**
   - Activated OSPF on routers to dynamically share routes.
   - Assigned OSPF areas and validated routes using the `show ip route` command.

### 4. **Testing and Validation**
   - **Inter-VLAN ping** to validate communication.
   - Verified OSPF convergence and routing paths.

## 🖼️ Network Diagram

Here’s a simplified view of the network topology used in this project:
![image_2025-01-01_175327892](https://github.com/user-attachments/assets/31f5c991-3635-48d5-9148-ffd7cbce93e3)


## 📝 Results and Learnings

- **Successful segmentation**: Traffic from each VLAN is isolated for enhanced security.
- **Inter-VLAN communication established**: Achieved through dynamic routing with OSPF.
- **Network flexibility**: OSPF ensures automatic route updates in case of topology changes.

## 📂 Project Structure

- **/configs**: Contains configuration files for switches and routers.
- **/screenshots**: Includes screenshots of connectivity tests and topology in Packet Tracer.
- **/documentation**: Detailed documentation, including commands used and explanations.

## 🔧 How to Reproduce This Project

1. Install [Cisco Packet Tracer](https://www.netacad.com/).
2. Import the `.pkt` file (provided in [Tools](https://github.com/glenn-77/Portfolio/blob/main/Tools/projet-ospf.pkt)).
3. Follow the commands to configure and test the network.
 - [Switch Configuration.txt](https://github.com/user-attachments/files/18286057/Switch.Configuration.txt)
 - [Router Configuration.txt](https://github.com/user-attachments/files/18286056/Router.Configuration.txt)

## 🏆 Skills Demonstrated

- VLAN configuration and management.
- Dynamic routing with OSPF.
- Network topology analysis and troubleshooting.

## 📬 Contact

If you have any questions or want to discuss this project, feel free to reach out via [my GitHub profile](https://github.com/glenn77).

---

Thank you for visit! 🙌

---
# Version Française

## Conception et Configuration d’un Réseau Sécurisé avec VLANs et Routage Dynamique (OSPF)

Ce projet illustre la création et la configuration d’un réseau sécurisé en utilisant des VLANs pour la segmentation du trafic, et le routage dynamique avec OSPF pour assurer une communication efficace et évolutive entre les différentes sous-réseaux.

## 🚀 Objectifs du Projet

1. **Segmenter le réseau local (LAN)** pour améliorer la sécurité et la gestion des flux avec des VLANs.
2. **Configurer le routage dynamique OSPF** pour permettre la communication entre les VLANs.
3. **Tester la connectivité et la sécurité du réseau** via des outils de simulation.

## 🛠️ Technologies et Outils Utilisés

- **Cisco Packet Tracer** : Simulation et configuration du réseau.
- **Protocoles réseau** : VLANs (802.1Q), OSPF (Open Shortest Path First).
- **Matériel simulé** : Switches, routeurs et PC.

## 📖 Étapes de Réalisation

### 1. **Création des VLANs**
   - VLAN 10 : Département informatique.
   - VLAN 20 : Département marketing.
   - VLAN 30 : Département RH.
   - VLAN 40 : Département Business.
   - Configuration des ports en mode **access** pour les utilisateurs et en mode **trunk** pour l’interconnexion entre les équipements réseau.

### 2. **Configuration de l’inter-VLAN**
   - Configuration des sous-interfaces sur le routeur :
     - `192.168.10.1/24` pour VLAN 10.
     - `192.168.20.1/24` pour VLAN 20.
     - `192.168.30.1/24` pour VLAN 30.
     - `192.168.40.1/24` pour VLAN 40.

### 3. **Mise en Place du Routage Dynamique OSPF**
   - Activation d’OSPF sur les routeurs pour partager les routes dynamiquement.
   - Attribution des zones OSPF et vérification des routes via `show ip route`.

### 4. **Tests et Validation**
   - **Ping inter-VLAN** pour valider la communication.
   - Vérification de la convergence OSPF et des chemins de routage.

## 🖼️ Diagramme Réseau

Voici une vue simplifiée de la topologie réseau utilisée dans ce projet :
![image_2025-01-01_175327892](https://github.com/user-attachments/assets/31f5c991-3635-48d5-9148-ffd7cbce93e3)


## 📝 Résultats et Apprentissage

- **Segmentation réussie** : Les flux de chaque VLAN sont isolés pour une meilleure sécurité.
- **Communication inter-VLAN établie** : Grâce au routage dynamique avec OSPF.
- **Flexibilité du réseau** : OSPF garantit une mise à jour automatique des routes en cas de changement de topologie.

## 📂 Structure du Projet

- **/configs** : Contient les fichiers de configuration pour les switches et routeurs.
- **/screenshots** : Captures d’écran des tests de connectivité et de la topologie dans Packet Tracer.
- **/documentation** : Documentation détaillée, incluant les commandes utilisées et les explications.

## 🔧 Comment Répliquer ce Projet

1. Installez [Cisco Packet Tracer](https://www.netacad.com/).
2. Importez le fichier `.pkt` (fourni dans [Outils](https://github.com/glenn-77/Portfolio/blob/main/Tools/projet-ospf.pkt)).
3. Suivez les commandes décrites pour configurer et tester le réseau.
   - [Switch Configuration.txt](https://github.com/user-attachments/files/18286057/Switch.Configuration.txt)
   - [Router Configuration.txt](https://github.com/user-attachments/files/18286056/Router.Configuration.txt)


## 🏆 Compétences Démontrées

- Configuration et gestion de VLANs.
- Routage dynamique avec OSPF.
- Analyse de la topologie réseau et résolution des problèmes.

## 📬 Contact

Si vous avez des questions ou souhaitez discuter de ce projet, n’hésitez pas à me contacter via [mon profil GitHub](https://github.com/glenn77).

---

Merci de votre visite ! 🙌

