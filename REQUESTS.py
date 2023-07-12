import requests

# URL de destino
url = "https://www.ejemplo.com"

# Realiza una solicitud HTTP GET
response = requests.get(url)

# Verifica el estado de la respuesta
if response.status_code == 200:
    # Imprime el contenido de la respuesta
    print(response.text)
else:
    print("Error al realizar la solicitud. Código de estado:", response.status_code)
