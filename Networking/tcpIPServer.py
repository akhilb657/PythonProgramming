import socket

host = "localhost"
port = 4000

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((host,port))

print("Server listening on port:",port)
s.listen(1)

c,addr = s.accept()

print("Connection from:",str(addr))

c.send(b"Hello, Magna")
c.send("welcome me".encode())
c.close()