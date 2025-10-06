import random
import time
from pymodbus.server import StartTcpServer
from pymodbus.datastore import ModbusDeviceContext, ModbusServerContext
from pymodbus.datastore import ModbusSequentialDataBlock
from threading import Thread
import numpy
import matplotlib.pyplot as plt

# Adresse du registre où la taille des vagues sera stockée
vague_REGISTER = 3
STATUS_COIL = 0
COIL_MOTEURALL= 1 
COIL_MOTEURSTOP= 2

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
    
    # Configuration des graphiques
    plt.ion()  # Mode interactif
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
    # Graphe sinusoïde
    line, = ax1.plot(temps_values, vague_values)
    ax1.set_ylabel('Hauteur des vagues (m)')
    ax1.set_title('Variation de la hauteur des vagues en temps réel')
    ax1.grid(True)
    # Graphe tout ou rien moteur
    moteurall_values = []
    moteurstop_values = []
    line_all, = ax2.plot(temps_values, moteurall_values, label='moteurall')
    line_stop, = ax2.plot(temps_values, moteurstop_values, label='moteurstop')
    ax2.set_ylabel('Etat moteur')
    ax2.set_xlabel('Temps (s)')
    ax2.set_yticks([0, 1])
    ax2.set_yticklabels(['OFF', 'ON'])
    ax2.set_title('Etat tout ou rien des moteurs')
    ax2.legend()
    ax2.grid(True)

    last_vague = None
    while True:
        status = context[slave_id].getValues(1, STATUS_COIL)[0]
        if status:  # Si la piscine fonctionne
            t = time.time() - start_time
            vague = offset + amplitude * math.sin(2 * math.pi * t / periode)
            context[slave_id].setValues(4, vague_REGISTER, [int(vague)])
            temps_values.append(t)
            vague_values.append(vague/10)
            # Etat des moteurs
            moteurall = context[slave_id].getValues(1, COIL_MOTEURALL)[0]
            moteurstop = context[slave_id].getValues(1, COIL_MOTEURSTOP)[0]
            moteurall_values.append(moteurall)
            moteurstop_values.append(moteurstop)
            if len(temps_values) > 50:
                temps_values.pop(0)
                vague_values.pop(0)
                moteurall_values.pop(0)
                moteurstop_values.pop(0)
            line.set_xdata(temps_values)
            line.set_ydata(vague_values)
            line_all.set_xdata(temps_values)
            line_all.set_ydata(moteurall_values)
            line_stop.set_xdata(temps_values)
            line_stop.set_ydata(moteurstop_values)
            ax1.relim()
            ax1.autoscale_view()
            ax2.relim()
            ax2.autoscale_view()
            fig.canvas.draw()
            fig.canvas.flush_events()
            # Détection de l'évolution de la vague
            if last_vague is not None:
                if vague > last_vague:
                    context[slave_id].setValues(1, COIL_MOTEURALL, [1])
                    context[slave_id].setValues(1, COIL_MOTEURSTOP, [0])
                    moteur_txt = "moteurall"
                elif vague < last_vague:
                    context[slave_id].setValues(1, COIL_MOTEURALL, [0])
                    context[slave_id].setValues(1, COIL_MOTEURSTOP, [1])
                    moteur_txt = "moteurstop"
                else:
                    moteur_txt = "moteur arrêter"
            else:
                moteur_txt = "moteur arrêter"
            last_vague = vague
        else:
            moteur_txt = "moteur arrêter"
        time.sleep(0.1)
        print(f"taille des vagues actuel: {vague/10:.1f}, status: {'ON' if status else 'OFF'} état moteur: {moteur_txt}")

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