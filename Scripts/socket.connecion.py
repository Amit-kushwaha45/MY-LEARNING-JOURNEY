#! /usr/bin/python3
import socket
#creat socket
s=socket.socket()
#define target
target_ip="127.0.0.1"#
change this to target ip
target_port=22#
change this to target port
s.connect((target_ip,port))
#if telling something
#s.send()
answer=s.recv(1024)
print(answer)
s.close()
