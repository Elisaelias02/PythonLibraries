from pwn import *

# Establecer la conexión con un proceso remoto
conn = remote('127.0.0.1', 1337)

# Recibir el mensaje de bienvenida
mensaje_bienvenida = conn.recvline()
print(mensaje_bienvenida)

# Enviar una cadena al proceso remoto
cadena = b'Hola, proceso remoto!\n'
conn.send(cadena)

# Recibir la respuesta del proceso remoto
respuesta = conn.recvline()
print(respuesta)

# Cerrar la conexión
conn.close()
