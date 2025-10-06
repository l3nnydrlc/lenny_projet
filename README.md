# **🌊 Piscine à Vagues Intelligente – Projet Python**


Nous sommes **deux entreprises indépendantes**, aux expertises complémentaires. Ce projet marque notre première **collaboration technique**, réunie autour d’un défi technologique innovant : développer un système intelligent pour une **piscine à vagues**.

- 🧪 **pHmetrics** : Spécialisée dans les systèmes de traitement de l’eau.
- 🌊 **SimuFluid** : Experte dans la simulation de mouvement et la gestion dynamique de fluides.

En conjuguant nos savoir-faire, nous visons à concevoir une solution intégrée, performante et durable.

---

## 🎯 Notre objectif


Développer une **piscine connectée et autonome**, capable de :

- Surveiller et réguler automatiquement le **taux de chlore** pour garantir une eau saine.
- Générer des **vagues dynamiques et réalistes** grâce à une modélisation physique (fonction sinusoïdale) interfacé avec des **capteurs et actionneurs**.

---

## 🔍 Présentation des modules


Le projet est divisé en **deux modules distincts**, chacun géré par l’une des entreprises :

## 🧪 pHmetrics – Gestion du Taux de Chlore


Cette partie du projet assuré par Lenny DERLICA assure une **qualité optimale de l’eau** en gérant automatiquement le taux de chlore pour avoir un pH neutre (7,2).

### 🔧 Composants

- **Capteur de taux de chlore** : Mesure en temps réel la concentration de chlore dans l'eau.
- **Actionneur** : Ajoute du pH+ ou du pH- selon les besoins.

---

### 🧠 Fonctionnement


 Si le taux de chlore ne correspond pas à la demande (7,2), le système ajuste automatiquement via l'actionneur pour maintenir un niveau sécurisé pour les nageurs. 🌡️

---

## 🌊 SimuFluid – Gestion des Vagues


Cette partie du projet assuré par Sacha IGNAM s'occupe de **générer des vagues dynamiques** pour une expérience de baignade fun et réaliste 🎢.

### 🔧 Composants

- **Capteur de mouvement (flotteur)** : Analyse les mouvements de surface pour estimer la hauteur des vagues.
- **Générateur de vagues** : Fonctionne selon une fonction sinusoïdale 🌀 pour simuler le mouvement naturel de l'eau.
 
---

### 🧠 Fonctionnement

Les données du capteur sont utilisées pour ajuster la sinusoïde qui pilote le moteur de vagues. Les vagues varie entre 0,5 et 2,5 mètres 🌊.

---


