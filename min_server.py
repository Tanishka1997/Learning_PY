import socket

s=socket.socket()
host=socket.gethostname()
port=1234
s.bind((host,port))
s.listen(5)
while True:
    c,addr=s.accept()
    c.send("Thank you for connecting")
    c.close()
    
