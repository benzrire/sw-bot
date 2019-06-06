# for action
import pyautogui
import base64
import cStringIO
import time
from random import randint

# for ocr tesseract and image comparison
import numpy as np
import pytesseract
import cv2

def getImageFromStatic(filename):
	with open('./static/' + filename, 'rb') as im:
		image = im.read()
		return base64.b64encode(image)

def randomDelay(start, stop):
	time.sleep(randint(start, stop)/1000)

def kType(str, interval):
	# type the characters in the str with delay interval between pressing each character key
	pyautogui.typewrite(str, interval=interval)

def kUp(key):
	# release the keyboard button up
	pyautogui.keyUp(key)

def kDown(key):
	# hold down the keyboard button
	pyautogui.keyDown(key)

def kPress(key):
	# press the keyboard button
	pyautogui.press(key)

def mDown(button):
	# hold down the mouse button
	pyautogui.mouseDown(button=button)

def mUp(button):
	# release the mouse button up
	pyautogui.mouseUp(button=button)

def mMoveTo(region, duration):
	# move to a random position in region over duration second(s)
	pyautogui.moveTo(randint(region[0], region[2]), randint(region[1], region[3]), duration)

def mClick(button):
	# single click the mouse with specify button('left', 'right', 'middle') at the mouse's current position
	pyautogui.click(button=button)

def mDoubleClick(button, interval):
	# double click the mouse with specify button at the mouse's current position but with interval second(s) pause in between double click
	pyautogui.click(button=button, clicks=2, interval=interval)

def captureRegion(region):
	# screenshot of the region and return base64 object
	buffer = cStringIO.StringIO()
	image = pyautogui.screenshot(region=(region[0], region[1], region[2] - region[0], region[3] - region[1]))
	image.save(buffer, format="png")
	return base64.b64encode(buffer.getvalue())

def ocr(image):
	# tesseract path
	pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract'

	# decode from base64 to image object
	img = cv2.imdecode(np.fromstring(base64.b64decode(image), dtype=np.uint8), 1)

	# convert color to grayscale
	img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	# tesseract image to text method
	return pytesseract.image_to_string(img).encode('utf-8')

def imageCompare(image1, image2):
	# decode from base64 to image object
	img1 = cv2.imdecode(np.fromstring(base64.b64decode(image1), dtype=np.uint8), 1)
	img2 = cv2.imdecode(np.fromstring(base64.b64decode(image2), dtype=np.uint8), 1)

	# initial sift object
	sift = cv2.xfeatures2d.SIFT_create()

	# detect keypoint and keypoint description
	kp1, des1 = sift.detectAndCompute(img1,None)
	kp2, des2 = sift.detectAndCompute(img2,None)

	# swap
	if len(kp1) > len(kp2):
		tkp = kp1
		tdes = des1
		kp1 = kp2
		des1 = des2
		kp2 = tkp
		des2 = tdes
		timg = img1
		img1 = img2
		img2 = timg

	# matching begin with flann(fast approximate nearest neighbors) algorithm
	FLANN_INDEX_KDTREE = 0
	INDEX_PARAM_TREES = 5
	SCH_PARAM_CHECKS = 50
	index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = INDEX_PARAM_TREES)
	search_params = dict(checks = SCH_PARAM_CHECKS)
	flann = cv2.FlannBasedMatcher(index_params,search_params)
	matches = flann.knnMatch(des1,des2,k=2)

	# counting matched keypoints
	matchesCount = 0
	for i,(m,n) in enumerate(matches):
	    if m.distance < 0.7*n.distance:
	        matchesCount += 1

	# return matched percentage
	return (matchesCount, (float(matchesCount)/float(len(des1)))*100)