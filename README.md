# **🌊 Piscine à Vagues Intelligente – Projet Python**

Nous sommes **deux entreprises indépendantes**, spécialisées dans les technologies embarquées et les systèmes automatisés. Ce projet marque notre première **collaboration technique autour d’un défi innovant** : créer un système intelligent pour une **piscine à vagues**.

- 🧪 **Entreprise 1** : Spécialisée dans les systèmes de traitement de l’eau.
- 🌊 **Entreprise 2** : Experte dans la simulation de mouvement et la gestion dynamique de fluides.

---

## 🎯 Notre objectif

Développer une **piscine connectée et autonome**, capable de :

- Surveiller et réguler automatiquement le **taux de chlore** pour garantir une eau saine.
- Générer des **vagues dynamiques et réalistes** grâce à une modélisation physique (fonction sinusoïdale) interfacé avec des **capteurs et actionneurs**.

---

## 🔍 Présentation des modules

Le projet est divisé en **deux modules distincts**, chacun géré par l’une des entreprises :

## 🧪 Entreprise 1 – Gestion du Taux de Chlore

Cette partie du projet assuré par Lenny DERLICA assure une **qualité optimale de l’eau** en gérant automatiquement le taux de chlore.

### 🔧 Composants
- **Capteur de taux de chlore** : Mesure en temps réel la concentration de chlore dans l'eau.
- **Actionneur** : Ajoute du pH+ ou du pH- selon les besoins.

---

### 🧠 Fonctionnement
> Si le taux de chlore ne correspond pas à la demande, le système ajuste automatiquement via l'actionneur pour maintenir un niveau sécurisé pour les nageurs. 🌡️

---

## 🌊 Entreprise 2 – Gestion des Vagues

Cette partie du projet assuré par Sacha IGNAM s'occupe de **générer des vagues dynamiques** pour une expérience de baignade fun et réaliste 🎢.

### 🔧 Composants
- **Capteur de pression** : Mesure la pression exercée par l'eau, utile pour la synchronisation des vagues.
- **Capteur de mouvement (flotteur)** : Analyse les mouvements de surface pour estimer la hauteur des vagues.
- **Générateur de vagues** : Fonctionne selon une fonction sinusoïdale 🌀 pour simuler le mouvement naturel de l'eau.
 
### 🧠 Fonctionnement
> Les données des capteurs sont utilisées pour ajuster la sinusoïde qui pilote le moteur de vagues. Les vagues sont donc adaptatives et sécurisées 🌊.

---

## 🗂️ Arborescence du Projet

