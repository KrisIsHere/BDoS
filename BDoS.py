#!/usr/bin/python
# -*- coding: utf-8 -*-


import os, sys, time
import socket, thread
import random
from threading import Lock

def en():
	loop = True
	while loop == True:
		targ = raw_input("Target (www.example.com): ")
		tar = raw_input("Threads: ")
		connections = raw_input("Amount of connections per thread: ")
		port = raw_input("Port: ")
		os.system("python2 BDoS/BDoS_en.py " + targ + " -t " + tar + " -c " + connections + " -p " + port)
def bg():
	targ = raw_input("Враг (www.example.com): ")
	tar = raw_input("Ботово: ")
	connections = raw_input("Брой връзки за всеки бот: ")
	port = raw_input("Порт: ")
	os.system("python2 BDoS/BDoS_bg.py " + targ + " -t " + tar + " -c " + connections + " -p " + port)
ascii = ["""\x1b[1;33m
▀█████████▄  ████████▄   ▄██████▄     ▄████████
  ███    ███ ███   ▀███ ███    ███   ███    ███
  ███    ███ ███    ███ ███    ███   ███    █▀
 ▄███▄▄▄██▀  ███    ███ ███    ███   ███
▀▀███▀▀▀██▄  ███    ███ ███    ███ ▀███████████
  ███    ██▄ ███    ███ ███    ███          ███
  ███    ███ ███   ▄███ ███    ███    ▄█    ███
▄█████████▀  ████████▀   ▀██████▀   ▄████████▀  \x1b[1;97m

""", """

\x1b[1;31m@@@@@@@   @@@@@@@    @@@@@@    @@@@@@
@@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@
@@!  @@@  @@!  @@@  @@!  @@@  !@@
!@   @!@  !@!  @!@  !@!  @!@  !@!
@!@!@!@   @!@  !@!  @!@  !@!  !!@@!!
!!!@!!!!  !@!  !!!  !@!  !!!   !!@!!!
!!:  !!!  !!:  !!!  !!:  !!!       !:!
:!:  !:!  :!:  !:!  :!:  !:!      !:!
 :: ::::   :::: ::  ::::: ::  :::: ::
:: : ::   :: :  :    : :  :   :: : :   \x1b[1;97m

""", """
\x1b[1;32m▄▄▄▄· ·▄▄▄▄        .▄▄ ·
▐█ ▀█▪██▪ ██ ▪     ▐█ ▀.
▐█▀▀█▄▐█· ▐█▌ ▄█▀▄ ▄▀▀▀█▄
██▄▪▐███. ██ ▐█▌.▐▌▐█▄▪▐█
·▀▀▀▀ ▀▀▀▀▀•  ▀█▄▀▪ ▀▀▀▀ \x1b[1;97m
"""]

print random.choice(ascii)
def lan():
	loop = True
	while loop == True:
		lol = raw_input("Please select your language \033[92;40m(\033[0;33men\033[92;40m/\033[0;33mbg\033[92;40m)\x1b[1;97m: ")
		if lol == "bg":
		    os.system("mkdir .info")
		    os.system("touch .info/bg.py")
		    bg()
		elif lol == "en":
		    os.system("mkdir .info")
		    os.system("touch .info/en.py")
		    en()
		else:
			print("You mistyped please try again. ")

if os.path.isfile(".info/bg.py"):
    bg()
elif os.path.isfile(".info/en.py"):
	en()
else:
	lan()
