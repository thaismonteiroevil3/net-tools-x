import os
import socket

def ping(host):
    print(f"🔹 Pingando {host}...")
    os.system(f"ping -c 4 {host}")

def resolver_dns(hostname):
    try:
        ip = socket.gethostbyname(hostname)
        print(f"🔹 {hostname} resolve para {ip}")
    except socket.gaierror:
        print("❌ Não foi possível resolver o DNS.")

def verificar_porta(host, porta):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    resultado = sock.connect_ex((host, porta))
    if resultado == 0:
        print(f"✅ Porta {porta} aberta em {host}")
    else:
        print(f"❌ Porta {porta} fechada em {host}")
    sock.close()

if __name__ == "__main__":
    print("Ferramentas de Redes 🛠️")
    print("1. Ping")
    print("2. Resolver DNS")
    print("3. Verificar Porta")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        host = input("Digite o host: ")
        ping(host)
    elif opcao == "2":
        hostname = input("Digite o hostname: ")
        resolver_dns(hostname)
    elif opcao == "3":
        host = input("Host: ")
        porta = int(input("Porta: "))
        verificar_porta(host, porta)
    else:
        print("❌ Opção inválida.")
