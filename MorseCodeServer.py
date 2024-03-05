from playsound import playsound 
from time import sleep
import socket
import socket 
from PyEssnt_LoganTheCreator import pyEssnt

#Server-side code

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
server.bind(('000.000.0.000', 8000))
pyEssnt.type("Waiting for connection...")
server.listen()
client, addr = server.accept()
pyEssnt.clearShell()
print('Connected')
#Sending: server.send("").encode()
#Recieving: msg = client.recv(1024).decode()

#-----------------------




def dit():
    playsound('dit.wav')
def dah():
    playsound('dah.wav')
def wait():
    sleep(0.5)
morseCodeDictionary = {
    ' ':'|',
    'a':'.-',
    'b':'-...',
    'c':'-.-.',
    'd':'-..',
    'e':'.',
    'f':'..-.',
    'g':'--.',
    'h':'....',
    'i':'..',
    'j':'.---',
    'k':'-.-',
    'l':'.-..',
    'm':'--',
    'n':'-.',
    'o':'---',
    'p':'.--.',
    'q':'--.-',
    'r':'.-.',
    's':'...',
    't':'-',
    'u':'..-',
    'v':'...-',
    'w':'.--',
    'x':'-..-',
    'y':'-.--',
    'z':'--..',
                       }
while True:
    client.send(input("Message: ").encode())

    text = client.recv(1024).decode('utf-8')


    morseCodeTable = str.maketrans(morseCodeDictionary)

    translatedToMorse = text.translate(morseCodeTable)

    for i in translatedToMorse:
        if i == '.':
            dit()
        elif i == '-':
            dah()
        elif i == '|':
            wait()
