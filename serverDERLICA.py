import random
import time
from pymodbus.server import StartTcpServer
from pymodbus.datastore import ModbusDeviceContext, ModbusServerContext
from pymodbus.datastore import ModbusSequentialDataBlock
from threading import Thread
import numpy
import matplotlib.pyplot as plt

# Adresse du registre où le pH sera stockée
pH_REGISTER = 0
pHplus_REGISTER = 1
pHmoins_REGISTER = 2
STATUS_COIL = 0

def pH_simulation(context, slave_id=0x00):
    """Simule une variation de pH toutes les secondes."""
    pH = 72  # pH initiale (ex: 7.2pH, multipliée par 10)
    while True:
        status = context[slave_id].getValues(1, STATUS_COIL)[0]
        if status:  # Si la piscine fonctionne
            # Variation aléatoire du pH
            pH += random.randint(-3, 3)
            if pH < 60:
                pH = 60
            if pH > 80:
                pH = 80
            if pH < 72:
                pHplus_REGISTER = 1
                pHmoins_REGISTER = 0
                pH += 1
            else:
                pHplus_REGISTER = 0
                pHmoins_REGISTER = 1
                pH -= 1 
            # Mise à jour du registre
            context[slave_id].setValues(4, pH_REGISTER, [pH])
        print(f"pH actuel: {pH/10:.1f}, status: {'ON' if status else 'OFF'}")

        time.sleep(1)

if __name__ == "__main__":
    # Création du datastore Modbus avec un registre de 10 mots
    device = ModbusDeviceContext(
        co=ModbusSequentialDataBlock(0, [True]*10),    # en marche initialement
        ir=ModbusSequentialDataBlock(0, [72]*10)  # 7.2 pH initial
    )
    context = ModbusServerContext(devices=device, single=True)

    # Lancement du thread de simulation de pH
    sim_thread = Thread(target=pH_simulation, args=(context,))
    sim_thread.daemon = True
    sim_thread.start()

    # Démarrage du serveur Modbus TCP sur le port 502
    print("Serveur Modbus TCP démarré sur le port 502...")
    StartTcpServer(context, address=("127.0.0.1", 502))

