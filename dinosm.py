from PIL import Image
# from PIL import ImageGrab ,for windows and macOS
import mss
import pyautogui
import time

def chk(sct):
	mss_image=sct.grab(sct.monitors[1]) #mss object
	print(type(mss_image))

	im = Image.frombytes("RGB",mss_image.size,mss_image.bgra,"raw","BGRX").convert('L')

	data = im.load()
	for x in range(460,475):
		for y in range(227,255):
			data[x,y] = 0 

	for x in range(460,475):
		for y in range(200,223):
				data[x,y] = 100

	im.show()
	#im.save('tt.png')

def act(sct):
	mss_image=sct.grab(sct.monitors[1]) #mss object
	im = Image.frombytes("RGB",mss_image.size,mss_image.bgra,"raw","BGRX").convert('L')
	'''there is a bug in PIL module which does not let frombyte fuction to convert image directly to 
	grayscale (denoted by L) once its fixed you can use L directly in place of RGB as a argument'''
	data = im.load()

	for x in range(500,525):
		for y in range(200,223):
			#print("in x")
			if data[x,y] < 200 :
				pyautogui.keyDown("down")
				time.sleep(0.25)
				pyautogui.keyUp("down")

				return


	for x in range(500,525):
		for y in range(227,255):
			#print("in x")
			if data[x,y] < 200 :
				pyautogui.press("up") 
				return
			

	return

def start(sct):
	print('starting')
	time.sleep(2)
	pyautogui.press("up")
	while True:
		act(sct)

#
with mss.mss() as sct:
	start(sct)
	#chk(sct)

