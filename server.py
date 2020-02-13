# this is for communication between the client and the server.
# client will send commands and server will execute

import socket
from sounds import speak
from os import system, name
from multiprocessing import Process
from datetime import datetime
import time

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)


def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')

def timePlay(checkFile):
    while True:
        now = datetime.now()
        dt_string = now.strftime("%H:%M:%S")
        hours = now.strftime("%H")
        minutes = now.strftime("%M")
        seconds = now.strftime("%S")
        zone = now.strftime("%p")
        if((int(seconds) == 0 and int(minutes) == 0)or checkFile):
            print("date and time =", dt_string)
            if checkFile:
                speak('The time is , ' + str(int(hours)%12) + ', ' + minutes + ', ' + zone)
                # checkFile = False
                break
            else:
                speak('The time is ,' + str(int(hours)) + ', ' + zone)
            time.sleep(1)




# timePlay()

def connection():
    flag = False
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        while True:
            s.listen()
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                conn.send(b'Connected!\nType quit to exit...\nType help for options\n\nCreated by Brian Culberson (KD8SYY)') 
                while True:
                    try:
                        data = conn.recv(1024)
                    except ConnectionResetError:
                        print("Connection Lost...")
                        break

                    if flag:
                        conn.send(b'Playing...')
                        speak(data.decode("utf-8"))
                        flag = False
                    else:
                        if data == b'quit':
                            conn.send(b'Connection Closed')
                            conn.close()
                            break
                        elif data == b'\nquit':
                            conn.send(b'\nConnection Closed')
                            conn.close()
                            break
                        elif data == b'speak':
                            conn.send(b'Enter desired Sentence:')
                            flag = True
                        elif data == b'time':
                            conn.send(b'Playing the time...')
                            timePlay(True)
                        else:
                            conn.send(b'That command is not reconized...')
            

if __name__ == '__main__':
    Process(target = timePlay, args=(False, )).start()
    Process(target = connection).start()
    clear()