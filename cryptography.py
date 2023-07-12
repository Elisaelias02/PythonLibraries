from cryptography.fernet import Fernet

# Genera una clave aleatoria para el cifrado
clave = Fernet.generate_key()

# Crea un objeto Fernet con la clave generada
cipher_suite = Fernet(clave)

# Mensaje original a cifrar
mensaje_original = "¡Hola, este es un mensaje secreto!"

# Cifra el mensaje
mensaje_cifrado = cipher_suite.encrypt(mensaje_original.encode())

print("Mensaje cifrado:", mensaje_cifrado)

# Descifra el mensaje
mensaje_descifrado = cipher_suite.decrypt(mensaje_cifrado).decode()

print("Mensaje descifrado:", mensaje_descifrado)