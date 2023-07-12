import nmap

# Crea un objeto de escaneo
nm = nmap.PortScanner()

# Especifica el rango de direcciones IP a escanear
ip_range = "192.168.1.1-10"

# Realiza un escaneo de puertos en el rango especificado
nm.scan(hosts=ip_range, arguments="-p 1-1000")

# Recorre los resultados del escaneo
for host in nm.all_hosts():
    print("Host:", host)
    for port in nm[host]["tcp"]:
        print("Puerto:", port, "Estado:", nm[host]["tcp"][port]["state"])
