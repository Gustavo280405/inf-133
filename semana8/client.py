import requests

url = 'http://localhost:5000/'

response = requests.get(url)

if response.status_code == 200:
    print("Respuesta del servidor:")
    print(response.text)
else:
    print("Error al conectar con el servidor:", response.status_code)

params = {'nombre': 'Gus'}
response = requests.get(url+'saludar', params=params)

if response.status_code == 200:
    data = response.json()
    mensaje = data['mensaje']
    print("Respuesta del servidor (GET):", mensaje)
else:
    print("Error al conectar con el servidor (GET):", response.status_code)

parametros={'a':2, 'b':3}
response = requests.get(url+'sumar',params=parametros)

if response.status_code == 200:
    data = response.json()
    mensaje = data['respuesta']
    print("Respuesta del servidor (GET):", mensaje)
else:
    print("Error al conectar con el servidor (GET):", response.status_code)

parametros={'pal':"reconoce"}
response = requests.get(url+'palin',params=parametros)

if response.status_code == 200:
    data = response.json()
    mensaje = data['palin']
    print("Respuesta del servidor (GET):", mensaje)
else:
    print("Error al conectar con el servidor (GET):", response.status_code)

parametros={'pal':"paralelepipedo", 'voc':"a"}
response = requests.get(url+'cont',params=parametros)

if response.status_code == 200:
    data = response.json()
    mensaje = data['cont']
    print("Respuesta del servidor (GET):", mensaje)
else:
    print("Error al conectar con el servidor (GET):", response.status_code)