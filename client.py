# client.py
 
import socket
#socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connect to server
# server_ip = '192.168.10.70'
# server_port = 9999
# print(f"connecting to server {server_ip}...... ")
s.connect(("localhost", 9999))
# print(f"connected to server sucessfully to {server_ip} ")
#recv
while True:
    print("server: ",s.recv(1024).decode())
    message = input('#>>>')
    s.send(message.encode())
 
#close
s.close()