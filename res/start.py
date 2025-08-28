import os
import configparser
import json
import time
from colorama import Fore, Back, Style, init

config = configparser.ConfigParser()
config.read('res/config.ini')

content = """[Settings]
lang="en"
"""

menu="main"

try:
	lang = config['Settings']['lang']
except:
	print("Error setting language! Creating new \"config.ini\" file...")
	with open('res/config.ini', 'w') as file:
		file.write(content)
	lang = config['Settings']['lang']

with open(f'res/lang/{lang.replace('"', '')}.json', 'r') as f:
	data = json.load(f)

name = data["init"]["nameprogram"]
init(autoreset=True)

def printname():
	print(Style.BRIGHT + name, Style.DIM + data["init"]["version"])
	print("-" * len(name))

def frame(frame=0):
	if frame==0:
		return "-    "
	elif frame==1:
		return "=-   "
	elif frame==2:
		return "-=-  "
	elif frame==3:
		return " -=- "
	elif frame==4:
		return "  -=-"
	elif frame==5:
		return "   -="
	elif frame==6:
		return "    -"
	elif frame==7:
		return "     "

def listfiles(isDir):
	# Get the current working directory as a string
	current_directory = os.getcwd()
	# Get a list of files and directories in the current directory
	file_list = os.listdir(current_directory)
	
	folders=[]
	files=[]
	
	# Iterate through each entry in the file list
	for entry in file_list:
		# Join the current directory path with the entry name
		fullpath = os.path.join(current_directory, entry)
		if os.path.isdir(fullpath):
			folders.append(entry)
		else:
			files.append(entry)
	
	if isDir:
		return folders
	else:
		return files

def open():
#	aframe=0
#	while True:
#		framestr=frame(int(aframe%8))
#		print(framestr, end="\r")
#		aframe+=1
#		time.sleep(0.2)
	#fneakjt
	os.system("clear")
	print(Style.BRIGHT + data["filemanager"]["selfile"])
	print("-"*12)
	for entry in listfiles(True):
		print(Fore.LIGHTGREEN_EX + entry)
	for entry in listfiles(False):
		print(Fore.WHITE + entry)
	input(data["filemanager"]["input"])

def main():
	print(f"(N) {data["project"]["newproj"]}")
	print(f"(O) {data["project"]["opnproj"]}")
	print(f"(E) {data["project"]["exit"]}")
	#...input...
	try:
		usrinp=input(">")
	except KeyboardInterrupt:
		init()
	if usrinp=="N" or usrinp=="n":
		#place holdero
		#e
		#a. SFDBGJKSJKTGKDHSSGSKWKHJC
		#createnew()
		pass
	elif usrinp=="O" or usrinp=="o":
		#eh,m
		#EHMERO.
		#EHMMARMOAOMAOIRO....
		open()
		pass
	elif usrinp=="E" or usrinp=="e":
		exit()
		pass
	else:
		#
		#
		init()
		pass
	pass

def init():
	while True:
		os.system("clear")
		printname()
		if menu == "main":
			main()

init()
