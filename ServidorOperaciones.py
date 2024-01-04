import socket
from _thread import *
from time import sleep

def hilo(cs):
    datos = []
    i = cs.recv(1024).decode("ascii")
    sleep(0.2)
    if (i == '1'):
        n1 = cs.recv(1024).decode("ascii")
        sleep(0.2)
        n2 = cs.recv(1024).decode("ascii")
        r = sum(n1,n2)
        cs.send(r.encode("ascii"))

    elif (i == '2'):
        n1 = cs.recv(1024).decode("ascii")
        sleep(0.2)
        n2 = cs.recv(1024).decode("ascii")
        r = res(n1,n2)
        cs.send(r.encode("ascii"))

    elif (i == '3'):
        n1 = cs.recv(1024).decode("ascii")
        sleep(0.2)
        n2 = cs.recv(1024).decode("ascii")
        r = mult(n1,n2)
        cs.send(r.encode("ascii"))

    elif (i == '4'):
        n1 = cs.recv(1024).decode("ascii")
        sleep(0.2)
        n2 = cs.recv(1024).decode("ascii")
        r = div(n1,n2)
        cs.send(r.encode("ascii"))

    elif (i == '5'):
        n1 = cs.recv(1024).decode("ascii")
        sleep(0.2)
        n2 = cs.recv(1024).decode("ascii")
        r = exp(n1,n2)
        cs.send(r.encode("ascii"))

    elif (i == '6'):
        n1 = cs.recv(1024).decode("ascii")
        sleep(0.2)
        n2 = cs.recv(1024).decode("ascii")
        r = mod(n1,n2)
        cs.send(r.encode("ascii"))
        
    else:
        datos.append(i)
        tipo = cs.recv(1024).decode("ascii")
        datos.append(tipo)
        servers.append(datos)
        print(servers)
        datos = []
    cs.close()

def sum(n1, n2):
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    h = socket.gethostname()
    puerto = ""
    for x in servers:
        if (x[0] == "suma"):
            puerto = x[1]
    ss.connect((h, int(puerto)))
    ss.send(str(n1).encode("ascii"))
    sleep(0.2)
    ss.send(str(n2).encode("ascii"))
    resp = ss.recv(1024).decode("ascii")
    ss.close()
    return resp

def res(n1, n2):
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    h = socket.gethostname()
    puerto = ""
    for x in servers:
        if (x[0] == "resta"):
            puerto = x[1]
    ss.connect((h, int(puerto)))
    ss.send(str(n1).encode("ascii"))
    sleep(0.2)
    ss.send(str(n2).encode("ascii"))
    resp = ss.recv(1024).decode("ascii")
    ss.close()
    return resp

def mult(n1, n2):
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    h = socket.gethostname()
    puerto = ""
    for x in servers:
        if (x[0] == "mult"):
            puerto = x[1]
    ss.connect((h, int(puerto)))
    ss.send(str(n1).encode("ascii"))
    sleep(0.2)
    ss.send(str(n2).encode("ascii"))
    resp = ss.recv(1024).decode("ascii")
    ss.close()
    return resp

def div(n1, n2):
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    h = socket.gethostname()
    puerto = ""
    for x in servers:
        if (x[0] == "div"):
            puerto = x[1]
    ss.connect((h, int(puerto)))
    ss.send(str(n1).encode("ascii"))
    sleep(0.2)
    ss.send(str(n2).encode("ascii"))
    resp = ss.recv(1024).decode("ascii")
    ss.close()
    return resp

def exp(n1, n2):
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    h = socket.gethostname()
    puerto = ""
    for x in servers:
        if (x[0] == "exp"):
            puerto = x[1]
    ss.connect((h, int(puerto)))
    ss.send(str(n1).encode("ascii"))
    sleep(0.2)
    ss.send(str(n2).encode("ascii"))
    resp = ss.recv(1024).decode("ascii")
    ss.close()
    return resp
def mod(n1, n2):

    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    h = socket.gethostname()
    puerto = ""
    for x in servers:
        if (x[0] == "mod"):
            puerto = x[1]
    ss.connect((h, int(puerto)))
    ss.send(str(n1).encode("ascii"))
    sleep(0.2)
    ss.send(str(n2).encode("ascii"))
    resp = ss.recv(1024).decode("ascii")
    ss.close()
    return resp

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 2000
servers = []
ss.bind((host, port))
print("Servidor listo")
ss.listen(50)
cont = 0
while True:
    cs, addr = ss.accept()
    print ("Conexion con ", str(addr))
    start_new_thread(hilo, (cs, ))   
    cont += 1
    if (cont == 50):
        print("Limite de usos alcanzado")
        break
ss.close()