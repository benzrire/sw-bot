# GGbot

## important

สำหรับ python version 3.4 ขึ้นไปจะไม่ซัพพอร์ตโมดูล cStringIO ให้แก้ method captureRegion ใน module.py จาก
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
  - [opencv](https://pypi.org/project/opencv-python/) เป็น image processing module
  - [pytesseract](https://pypi.org/project/pytesseract/) เป็น tesseract ocr module
  - [matplotlib](https://matplotlib.org/users/installing.html) (optional module, easy debugging)
  
## installation
1. สร้าง folder ชื่อ 'static' เพื่อเก็บรูปภาพที่คาดว่าจะใช้ในการ compare image เพราะ method getImageFromStatic จะเข้าไปดึงรูปจากใน 'static' folder
2. แก้ไข path ของ tesseract executable file ที่เราติดตั้งไว้ ในไฟล์ module.py method name 'ocr'
```
# tesseract path
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract'
```

## example usage
1. สร้างไฟล์ main.py
```
import module as _

def main():
  _.mMoveTo([100, 100, 500, 500], 0.1)
  _.mClick('left')

if __name__ == '__main__':
  main()
```
2. run powershell command
```
python ./main.py
```
