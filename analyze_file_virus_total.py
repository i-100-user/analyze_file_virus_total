import hashlib
from virus_total_apis import PublicApi
import os
import sys

# Asegúrate de que el usuario proporcionó el nombre del archivo como argumento
if len(sys.argv) != 2:
    print("Uso: python script.py <nombre_del_archivo>")
    sys.exit(1)

# API key de VirusTotal
api_key = "652df9fe066a6b829061b3ee410dffa5517d154a84f73f65de347f9ef317a364"

# Nombre del archivo pasado como argumento
file_name = sys.argv[1]

# Verifica si el archivo existe
if not os.path.isfile(file_name):
    print(f"El archivo {file_name} no existe.")
    sys.exit(1)

# Crea una instancia de la API de VirusTotal
api = PublicApi(api_key)

# Calcula el hash MD5 del archivo
with open(file_name, 'rb') as file:
    file_hash = hashlib.md5(file.read()).hexdigest()

# Obtén el informe del archivo usando el hash
respuesta = api.get_file_report(file_hash)

# Verifica la respuesta de la API y toma las acciones correspondientes
if respuesta['response_code'] == 200:
    if respuesta['results']['positives'] > 0:
        print("\033[91m\t\n[x] Archivo malicioso\n\033[0m")  
        print("Archivo eliminado.")
        os.remove(file_name)
    else:
        print("\033[92m\t\n[+] Archivo seguro\n\033[0m")  
else:
    print("No se ha podido obtener el análisis del archivo.")


        