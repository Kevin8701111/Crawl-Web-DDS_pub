#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 zack <zack@zack>
#
# Distributed under terms of the MIT license.

"""
"""
import requests
import time
import json
import os, sys
import socket
from flask import Flask
from flask_restful import Resource, Api

hostname = '192.168.8.11'                                       #chang to your service IP
port = '8080'                                                   #chang to your service Port

def get():
    response = os.system('ping -c 1 ' + hostname)
    #print(response)
    if (response == 0):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((hostname, int(port)))
        if result == 0:
            sock.close()
            distance = 'http://' + hostname + ':' + port
            #print(distance)
            r = requests.get(distance)
            #print(r)
            #print(r.content)
            value = r.content.decode('utf-8')
            resp = '{"message":' + '"connect"}'
            return json.loads(value)
        else:
            resp = '{"message":' + '"connect-error" }'
            return json.loads(resp)
    else:
         resp = '{"message":' + '"network-error"}'
         #print(resp)
         json.loads(resp)



#-----------------------------------------------------------------------------------------------------

bind_ip = "10.21.20.210"
def main(send_port):
    send_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    send_socket.connect((bind_ip,send_port))
    str_test = json.dumps(test)
    while(1):
        d = input("select 1(continue) or -1(go out):")
        if d=="-1":
            send_socket.close()
            break
        else:
            test = get();
            d ='{"active":"create","cmd":"./subscriber -DCPSConfigFIle rtps.ini","topic":"UPS"}'
            print (d)
            send_socket.send(d.encode())
            str_test = str(test).split(",")
            for str_test in str_test:
                 d='{"send":"{\\"from\\":\\"7610307082307919\\",\\"message\\":\\"'+ str_test + ' \\"}"}'
            #d = '{"send":"{\\"from\\":\\"7610307082307919\\",\\"message\\":\\"一\\"}"}'
                 print (d +"\n")
                 send_socket.send(d.encode())
                 time.sleep(1)
                 print (send_socket.recv(1024))

if __name__ =="__main__":
    send_port = int(input("port "))
    main(send_port)
