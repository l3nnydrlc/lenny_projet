# ModBus TCP Serveur et Client en Python

Ce projet utilise Python et la bibliothèque pymodbus pour créer un serveur et un client ModBus TCP avec des outils de développement modernes.

## 🛠️ Environnement de Développement

### Prérequis Système

- **Système d'exploitation** : Linux, macOS ou Windows avec WSL2 recommandé
- **Git** : Pour le contrôle de version et le clonage de ce dépôt
- **UV** : Gestionnaire moderne de paquets Python d'Astral

### Installation des Outils

#### 1. Installation de Git

**Sur Ubuntu/Debian :**
```bash
sudo apt update
sudo apt install gi
```

**Sur macOS avec Homebrew :**
```bash
brew install git
```

**Sur Windows :**
- Téléchargez Git depuis [git-scm.com](https://git-scm.com/download/win)
- Ou utilisez Winget : `winget install Git.Git`

#### 2. Installation de UV

UV est un gestionnaire de paquets et environnements Python ultra-rapide développé par Astral.

**Installation globale :**
```bash
# Sur Linux/macOS
curl -LsSf https://astral.sh/uv/install.sh | sh

# Sur Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Alternative avec pip (si Python est déjà installé)
pip install uv
```

**Vérification de l'installation :**
```bash
uv --version
```

## 🚀 Installation du Projet

### Méthode recommandée avec UV

1. **Cloner le repository avec Git :**
```bash
git clone https://github.com/Kryll13/demomodbus.git
cd demomodbus
```

2. **Installer et configurer Python avec UV :**
```bash
# UV installera automatiquement la version de Python spécifiée
uv python install 3.13

# Vérifier que Python 3.13 est disponible
uv python list
```

3. **Créer l'environnement virtuel et installer les dépendances :**
```bash
# Synchroniser l'environnement avec le fichier pyproject.toml
uv sync

# Activer l'environnement virtuel
source .venv/bin/activate  # Linux/macOS
# ou .venv\Scripts\activate  # Windows
```

## 📦 Structure du Projet

```
demomodbus/
├── .venv/                 # Environnement virtuel (créé par UV)
├── server.py              # Serveur ModBus
├── client.py              # Client ModBus
├── pyproject.toml         # Configuration UV et dépendances
├── requirements.txt       # dépendances seulement
├── README.md              # Documentation
├── LICENSE                # Licence GPL 3.0 BY-CC
```

### Configuration UV (pyproject.toml)

```toml
[project]
name = "demomodbus"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.13"
dependencies = [
    "pymodbus>=3.11.2",
]
```

## 🖥️ Serveur ModBus

### Code source : `server.py`

```python
from pymodbus.server import StartTcpServer
from pymodbus.datastore import ModbusSequentialDataBlock, ModbusDeviceContext, ModbusServerContext

# Initialisation des données (coils, holding registers, etc.)
store = ModbusDeviceContext(
    di=ModbusSequentialDataBlock(0, [0]*100),    # Discrete Inputs
    co=ModbusSequentialDataBlock(0, [0]*100),    # Coils
    hr=ModbusSequentialDataBlock(0, [13]*100),   # Holding Registers
    ir=ModbusSequentialDataBlock(0, [0]*100)     # Input Registers
)

# Contexte du serveur (1 slave par défaut, unit_id=1)
context = ModbusServerContext(devices = store, single=True)

# Démarrer le serveur sur le port 5020
StartTcpServer(context=context, address=("0.0.0.0", 502))
```

### Lancement du serveur :

```bash
# Avec UV
uv run server.py

# Ou avec l'environnement activé
python server.py
```

## 📱 Client ModBus

### Code source : `client.py`

```python
from pymodbus.client import ModbusTcpClient

# Connexion au serveur Modbus
client = ModbusTcpClient('127.0.0.1', port=502)
client.connect()

# Lecture de registres
result = client.read_holding_registers(address=0)
if not result.isError():
    print("Valeurs des registres:", result.registers)

# Écriture dans un registre
client.write_register(address=0, value=17)

client.close()
```

### Lancement du client :

```bash
uv run client.py
```

## 🎯 Commandes UV Utiles

```bash
# Installer une version spécifique de Python
uv python install 3.13

# Lister les versions de Python disponibles
uv python list

# Synchroniser les dépendances
uv sync

# Lancer des scripts
uv run server.py
uv run client.py

# Ajouter une dépendance
uv add nom-du-paquet

# Mettre à jour les dépendances
uv update

# Lister les dépendances
uv list
```

## 🔧 Rappel de gestion des versions avec Git

```bash
# Initialiser le dépôt Git (si ce n'est pas déjà fait)
git init

# Ajouter les fichiers
git add .

# Premier commit
git commit -m "Initial commit: Serveur et client ModBus"

# Configurer le dépôt distant
git remote add origin <url-du-repo>

# Pousser les changements
git push -u origin main
```

## 📊 Types de registres ModBus

| Type | Accès | Description | Adressage |
|------|-------|-------------|-----------|
| Coils | Read/Write | Sorties booléennes | 0-99 |
| Discrete Inputs | Read-only | Entrées booléennes | 0-99 |
| Holding Registers | Read/Write | Registres 16-bit | 0-99 |
| Input Registers | Read-only | Registres d'entrée 16-bit | 0-99 |

## 🐛 Dépannage

**Problèmes courants :**

1. **Port 502 indisponible :**
```bash
# Changer le port dans le code
# ou utiliser sudo sur Linux
sudo uv run server.py
```

2. **Problèmes avec UV :**
```bash
# Réinitialiser l'environnement
uv clean
uv sync

# Vérifier la version de Python
uv python list
```

3. **Problèmes Git :**
```bash
# Configurer Git si ce n'est pas déjà fait
git config --global user.name "Votre Nom"
git config --global user.email "votre.email@example.com"
```

## 📖 Ressources Complémentaires

- [Documentation pymodbus](https://pymodbus.readthedocs.io/) ❗3.11
- [Documentation UV](https://github.com/astral-sh/uv)
- [Guide Git](https://git-scm.com/doc)
- [Cours Git](https://buzut.net/cours/versioning-avec-git/comprendre-git-et-le-versioning) 👍Merci Quentin !
- [Spécification ModBus](https://modbus.org/specs.php)
- [Python 3.13 Documentation](https://docs.python.org/3.13/)


---

Développé pour l'enseignement de ModBus avec Python 3.13, UV et Git 🐍⚡📚

## 🌊 Piscine à Vagues Intelligente – Projet Python

Bienvenue dans notre projet collaboratif visant à créer une **piscine à vagues intelligente**, connectée et autonome grâce à des capteurs, actionneurs et une gestion en Python 🐍.

Ce projet est réalisé par **deux entreprises indépendantes** qui collaborent autour de deux modules distincts :

---

## 🧪 Entreprise 1 – Gestion du Taux de Chlore

Cette partie du projet assure une **qualité optimale de l’eau** en gérant automatiquement le taux de chlore.

### 🔧 Composants
- **Capteur de chlore** : Mesure en temps réel la concentration de chlore dans l'eau.
- **Actionneur** : Ajoute ou retire du chlore selon les besoins.

### 🧠 Fonctionnement
> Si le taux de chlore est trop bas ou trop haut, le système ajuste automatiquement via l'actionneur pour maintenir un niveau sécurisé pour les nageurs. 🌡️

---

## 🌊 Entreprise 2 – Gestion des Vagues

Cette partie du projet s'occupe de **générer des vagues dynamiques** pour une expérience de baignade fun et réaliste 🎢.

### 🔧 Composants
- **Capteur de pression** : Mesure la pression exercée par l'eau, utile pour la synchronisation des vagues.
- **Capteur de mouvement (flotteur)** : Analyse les mouvements de surface pour estimer la hauteur des vagues.
- **Générateur de vagues** : Fonctionne selon une fonction sinusoïdale 🌀 pour simuler le mouvement naturel de l'eau.

### 🧠 Fonctionnement
> Les données des capteurs sont utilisées pour ajuster la sinusoïde qui pilote le moteur de vagues. Les vagues sont donc adaptatives et sécurisées 🌊.

---

## 🗂️ Arborescence du Projet

