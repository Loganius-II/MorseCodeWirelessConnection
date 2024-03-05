from playsound import playsound 
from time import sleep
import socket


#Server-side code

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
client.connect(('192.168.1.140',8000))



#Sending: client.send("").encode()
#Recieving: msg = client.recv(1024).decode()

#-----------------------



while True:
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

    client.send(input("Message: ").encode())