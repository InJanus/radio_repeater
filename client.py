import socket

HOST = '127.0.0.1'#input("Input connecting address: ") #'127.0.0.1'  # The server's hostname or IP address
PORT = int(input("Input connecting port: ")) #65432        # The port used by the server
tryagainresult = True

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    while tryagainresult:
        try:
            s.connect((HOST, PORT))
            tryagainresult = False
            connect = True
        except ConnectionRefusedError:
            tryagain = input("Connection Refused, try again? (y,n): ")
            if tryagain == 'y':
                tryagainresult = True
            else: 
                tryagainresult = False   
    if(connect == True):
        data = s.recv(1024)
        print(data.decode("utf-8"))
    while connect == True: 
        try:
            sendData = str.encode(input(">"))
        except KeyboardInterrupt:
            sendData = b'\nquit'
        s.send(sendData)
        data = s.recv(1024)
        print(data.decode("utf-8"))
        if data.decode("utf-8") == "Connection Closed" or data.decode("utf-8") == "\nConnection Closed":
            connect = False