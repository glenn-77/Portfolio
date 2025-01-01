# Conception et Configuration d’un Réseau Sécurisé avec VLANs et Routage Dynamique (OSPF)

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
2. Importez le fichier `.pkt` (fourni dans `Outils`).
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

