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

import random
import time
from pymodbus.server import StartTcpServer
from pymodbus.datastore import ModbusDeviceContext, ModbusServerContext
from pymodbus.datastore import ModbusSequentialDataBlock
from threading import Thread

# Adresse du registre où le pH sera stockée
pH_REGISTER = 0
STATUS_COIL = 0

def pH_simulation(context, slave_id=0x00):
    """Simule une variation de pH toutes les secondes."""
    pH = 72  # pH initiale (ex: 7.2pH, multipliée par 10)
    while True:
        status = context[slave_id].getValues(1, STATUS_COIL)[0]
        if status:  # Si la piscine fonctionne
            # Variation aléatoire du pH
            pH += random.randint(-0.5, 0.5)
            if pH < 50:
                pH = 50
            if pH > 90:
                pH = 90
            # Mise à jour du registre
            context[slave_id].setValues(3, pH_REGISTER, [pH])

        time.sleep(1)

if __name__ == "__main__":
    # Création du datastore Modbus avec un registre de 10 mots
    device = ModbusDeviceContext(
        co=ModbusSequentialDataBlock(0, [True]*10),    # en marche initialement
        hr=ModbusSequentialDataBlock(0, [72]*10)  # 7.2 pH initial
    )
    context = ModbusServerContext(devices=device, single=True)

    # Lancement du thread de simulation de pH
    sim_thread = Thread(target=pH_simulation, args=(context,))
    sim_thread.daemon = True
    sim_thread.start()

    # Démarrage du serveur Modbus TCP sur le port 502
    print("Serveur Modbus TCP démarré sur le port 502...")
    StartTcpServer(context, address=("0.0.0.0", 502))
