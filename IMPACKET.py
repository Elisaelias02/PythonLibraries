from impacket import smb
from impacket import smbconnection

# Información de autenticación
usuario = "usuario"
contraseña = "contraseña"
dominio = "dominio"
ip_destino = "127.0.0.1"

# Establecer la conexión SMB
conn = smbconnection.SMBConnection(ip_destino, ip_destino)
conn.login(user=usuario, password=contraseña, domain=dominio)

# Enumerar usuarios
enumerador = smb.SMBEnumerateUsers(conn)
usuarios = enumerador.getUsers()

# Imprimir usuarios
for usuario in usuarios:
    print(usuario.decode())
