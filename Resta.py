import socket
from _thread import *
from time import sleep

def conexion():
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    h = socket.gethostname()
    ss.connect((h, 2000))
    ss.send("resta".encode("ascii"))
    sleep(0.2)
    ss.send("2002".encode("ascii"))
    ss.close()
def op(cs):
    n1 = cs.recv(1024).decode("ascii")
    sleep(0.25)
    n2 = cs.recv(1024).decode("ascii")
    r = int(n1) - int(n2)
    cs.send(str(r).encode("ascii"))
    print("Cliente {} atendido satisfactoriamente".format(cont))
    cs.close()    
conexion()
ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 2002
ss.bind((host, port))
print("Servidor jalando al 100 padrino")
ss.listen(10)
cont = 0
while True:
    cs, addr = ss.accept()
    print("Conexion jalando con ", str(addr))
    start_new_thread(op, (cs, ))  
    cont += 1
    if (cont == 10):
        print("Lo vas a matar, ya llegó al límite padrino")
        break   
ss.close()
input("Enter para terminar padrinnoli.")