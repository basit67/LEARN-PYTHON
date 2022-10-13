from re import S
import socket
HOST = '127.0.0.1'
PORT = '7777'
S = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
S.connect((HOST,PORT))