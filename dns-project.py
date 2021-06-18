import socket
domain_name = ['python.org','eclipse.org','instagram.com','hp.com']
for i in domain_name:
    print("ip adress for ", i , ' is ' , socket.gethostbyname(i))
