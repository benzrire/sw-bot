# Summoners War Game Bot

> คำเตือน!! ทำใช้เอง ไม่การันตีโดนแบน5555 กรุณาใช้วิจารณญาณในการอ่าน และใช้งานด้วยเน้อ

## important

สำหรับเวอร์ชัน 1 ผมใช้ python 2.7.8 ถ้าใครใช้ python 3.4 ขึ้นไปถ้าจำไม่ผิด มันจะไม่ซัพพอร์ตโมดูล cStringIO ให้แก้ method captureRegion ใน module.py จาก
```
import cStringIO
...
def captureRegion(region):
  # screenshot of the region and return base64 object
	buffer = cStringIO.StringIO()
	image = pyautogui.screenshot(region=(region[0], region[1], region[2]-region[0], region[3]-region[1]))
	image.save(buffer, format="png")
	return base64.b64encode(buffer.getvalue())
```
เป็น
```
from io import BytesIO
...
def captureRegion(region):
	# screenshot of the region and return base64 object
	buffer = BytesIO()
	image = pyautogui.screenshot(region=(region[0], region[1], region[2]-region[0], region[3]-region[1]))
	image.save(buffer, format="png")
	return base64.b64encode(buffer.getvalue())
```

## requirement
- [python](https://www.python.org) 2 or 3
- [tesseract](https://www.github.com/UB-Mannheim/tesseract/wiki) ocr alpha ของ Mannheim University
- python package
  - [pyautogui](https://pyautogui.readthedocs.io/en/latest/introduction.html) เป็น windows action module
  - [opencv](https://pypi.org/project/opencv-python/) เป็น image processing lib
  - [pytesseract](https://pypi.org/project/pytesseract/) เป็น python module สำหรับใช้ tesseract
  
## installation
1. create folder name 'static' เอาไว้เก็บรูปภาพที่คาดว่าจะใช้ในการ compare image เพราะ method getImageFromStatic จะเข้าไปดึงรูปจากใน 'static' folder
2. แก้ไข path ของ tesseract executable file ที่เราติดตั้งไว้ ในไฟล์ module.py method name 'ocr' เช่น
```
# tesseract path
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract'
```

### ไว้กลับมาเขียน รีบบบบบ555
