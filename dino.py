from PIL import Image
# from PIL import ImageGrab ,for windows and macOS
import mss
import pyautogui
import time
from selenium import webdriver

def chk(sct):

	mss_image=sct.grab(sct.monitors[1]) #mss object
	print(type(mss_image))

	im = Image.frombytes("RGB",mss_image.size,mss_image.bgra,"raw","BGRX").convert('L')

	data = im.load()
	for x in range(415,160,-1):
		for y in range(435,400,-1):
			data[x,y] = 100 

	for x in range(415,160,-1):
		for y in range(520,500,-1):
			data[x,y] = 100

	# for x in range(450,160,-1):
	# 	for y in range(600,550,-1):
	# 		data[x,y] = 100


	im.show()


def dark_mode(data):

	for x in range(415,160,-1):
		for y in range(435,400,-1):
			
			if data[x,y] > 100 :#check for light obstacle
				pyautogui.keyDown("down")
				time.sleep(0.25)
				pyautogui.keyUp("down")

				return


	for x in range(415,160,-1):
		for y in range(520,500,-1):
			
			if data[x,y] > 100 :
				pyautogui.press("up") 
				return




def nomal_mode(data):

	for x in range(415,160,-1):
		for y in range(435,400,-1):
			
			if data[x,y] < 100 :#check for dark obstacle
				pyautogui.keyDown("down")
				time.sleep(0.25)
				pyautogui.keyUp("down")

				return


	for x in range(415,160,-1):
		for y in range(520,500,-1):
			
			if data[x,y] < 100 :
				pyautogui.press("up") 
				return


def act(sct):
	mss_image=sct.grab(sct.monitors[1]) #mss object
	im = Image.frombytes("RGB",mss_image.size,mss_image.bgra,"raw","BGRX").convert('L')
	'''there is a bug in PIL module which does not let frombyte fuction to convert image directly to 
	grayscale (denoted by L) once its fixed you can use L directly in place of RGB as an argument'''
	data = im.load()
	# 400,600 point which turns dark during dark mode
	#check if its colour is close to white

	if data[400,600]>220: 
		nomal_mode(data)
	else:
	#point is not close to white, game is in dark mode
		dark_mode(data)	



def start(sct):
	print('starting')
	time.sleep(2)
	pyautogui.press("up")
	time.sleep(2)
	

	while True:
		act(sct)

#
with mss.mss() as sct:
	driver = webdriver.Chrome()
	driver.maximize_window()
	driver.get('chrome://dino/')
	start(sct)
	#chk(sct)

