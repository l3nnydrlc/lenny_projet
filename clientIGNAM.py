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


print("attendre 5 secondes")
time.sleep(5)

client.write_coil(address=0, value=True)

client.write_coil(address=1, value=0)  # moteurall à 0
client.write_coil(address=2, value=0)  # moteurstop à 0
print("arrêt des moteurs pendant 5 secondes")
time.sleep(5)

client.close()