import random
import time
from pymodbus.server import StartTcpServer
from pymodbus.datastore import ModbusDeviceContext, ModbusServerContext
from pymodbus.datastore import ModbusSequentialDataBlock
from threading import Thread
import numpy
import matplotlib.pyplot as plt

# Adresse du registre où la taille des vagues sera stockée
vague_REGISTER = 1
STATUS_COIL = 0

def vague_simulation(context, slave_id=0x00):
    """Simule une variation sinusoïdale de la taille des vagues en fonction du temps."""
    import math
    start_time = time.time()
    amplitude = 10  # Amplitude de la sinusoïde (en dizaines de cm)
    periode = 15     # Période de la sinusoïde en secondes
    offset = 15     # Valeur moyenne de la sinusoïde (en dizaines de cm)
    
    # Listes pour stocker les données du graphique
    temps_values = []
    vague_values = []
    
    # Configuration du graphique
    plt.ion()  # Mode interactif
    fig, ax = plt.subplots()
    line, = ax.plot(temps_values, vague_values)
    ax.set_xlabel('Temps (s)')
    ax.set_ylabel('Hauteur des vagues (m)')
    ax.set_title('Variation de la hauteur des vagues en temps réel')
    ax.grid(True)
    
    while True:
        status = context[slave_id].getValues(1, STATUS_COIL)[0]
        if status:  # Si la piscine fonctionne
            # Calcul de la valeur sinusoïdale
            t = time.time() - start_time
            vague = offset + amplitude * math.sin(2 * math.pi * t / periode)
            # Mise à jour du registre
            context[slave_id].setValues(4, vague_REGISTER, [int(vague)])
            
            # Mise à jour des données du graphique
            temps_values.append(t)
            vague_values.append(vague/10)  # Conversion en mètres
            
            # Garder seulement les 50 dernières valeurs pour le graphique
            if len(temps_values) > 50:
                temps_values.pop(0)
                vague_values.pop(0)
            
            # Mise à jour du graphique
            line.set_xdata(temps_values)
            line.set_ydata(vague_values)
            ax.relim()
            ax.autoscale_view()
            fig.canvas.draw()
            fig.canvas.flush_events()

        print(f"taille des vagues actuel: {vague/10:.1f}, status: {'ON' if status else 'OFF'}")

        time.sleep(0.1)  # Mise à jour plus fréquente pour une animation plus fluide

if __name__ == "__main__":
    # Création du datastore Modbus avec un registre de 10 mots
    device = ModbusDeviceContext(
        co=ModbusSequentialDataBlock(0, [True]*10),    # en marche initialement
        ir=ModbusSequentialDataBlock(0, [10]*10)  # 1m taille des vagues initial
    )
    context = ModbusServerContext(devices=device, single=True)

    # Lancement du thread de simulation de la taille des vagues
    sim_thread = Thread(target=vague_simulation, args=(context,))
    sim_thread.daemon = True
    sim_thread.start()

    # Démarrage du serveur Modbus TCP sur le port 502
    print("Serveur Modbus TCP démarré sur le port 502...")
    StartTcpServer(context, address=("127.0.0.1", 502))
