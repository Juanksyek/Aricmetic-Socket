import socket
from time import sleep

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 2000
ss.connect((host, port))
print("Suma-------------(1)")
print("Resta------------(2)")
print("Multiplicacion---(3)")
print("Division---------(4)")
print("Exponente--------(5)")
print("Residuo----------(6)")
opc = input("Opcion: ")
while (opc != '1' and opc != '2' and opc != '3' and opc != '4' and opc != '5' and opc != '6'):
    print("Caracter invalido, ingresa otro padrino")
    opc = input("Opcion: ")
n1 = input("Primer número padrino: ")
n2 = input("Segundo número padrino: ")
ss.send(opc.encode("ascii"))
sleep(0.2)
ss.send(str(n1).encode("ascii"))
sleep(0.2)
ss.send(str(n2).encode("ascii"))
resp = ss.recv(1024).decode("ascii")
print("Resultado: {}".format(resp))
input("Enter para terminar.")