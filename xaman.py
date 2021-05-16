#!/usr/bin/python

import pyautogui as pag
import time

def rain():
	time.sleep(2)
	pag.click(415, 505)
	time.sleep(0.5)
	pag.click(383, 395)
	time.sleep(0)

def selectme():
	pag.click(38, 438)

def autocast():
	selectme()
	pag.typewrite(["1"])
	time.sleep(1)
	pag.typewrite(["0"])
	rain()
	time.sleep(1)
	chain()

def chain():
	while(True):
		pag.typewrite(["2"])
		time.sleep(0.5)


autocast()
