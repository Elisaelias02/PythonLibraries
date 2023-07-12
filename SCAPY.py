from scapy.all import IP, TCP, sr1

# Dirección IP de destino y rango de puertos a escanear
ip_destino = "127.0.0.1"
puertos = range(1, 100)

# Realiza un escaneo de puertos
for puerto in puertos:
    paquete = IP(dst=ip_destino) / TCP(dport=puerto, flags="S")
    respuesta = sr1(paquete, timeout=1, verbose=0)
    
    if respuesta is not None and respuesta.haslayer(TCP) and respuesta.getlayer(TCP).flags == 0x12:
        print(f"Puerto {puerto} abierto")
