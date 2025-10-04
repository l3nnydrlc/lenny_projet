from pymodbus.client import ModbusTcpClient
import time

# Connexion au serveur Modbus
client = ModbusTcpClient('127.0.0.1', port=502)
client.connect()

# Lecture de registres
result = client.read_input_registers(address=0)
if not result.isError():
    print("Valeurs des registres:", result.registers)

# Écriture dans un registre
client.write_coil(address=0, value=False)

print("attendre 2 secondes")
time.sleep(2)

client.write_coil(address=0, value=True)
# Exemple : écrire la valeur 17 dans le registre à l'adresse 0 (17.0°C)
# client.write_register(address=0, value=17)
client.write_coil(address=1, value=0)  # pHplus_status à 0
client.write_coil(address=2, value=0)  # pHmoins_status à 0
print("pHplus_status et pHmoins_status à 0 pendant 2 secondes")
time.sleep(2)
client.write_coil(address=1, value=1)  # pHplus_status à 1
print("pHplus_status à 1")


client.close()