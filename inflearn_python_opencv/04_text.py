"""
4. 텍스트
"""
# OpenCV에서 사용하는 글꼴 종류
## 1. cv2.FONT_HERSHEY_SIMPLEX: 보통 크기의 산 세리프(sans-serif) 글꼴
## 2. cv2.FONT_HERSHEY_PLAIN : 작은 크기의 산 세리프 글꼴
## 3. cv2.FONT_HERSHEY_SCRIPT_SIMPLEX : 필기체 스타일 글꼴
## 4. cv2.FONT_HERSHEY_TRIPLEX : 보통 크기의 세리프 글꼴
## 5. cv2.FONT_ITALIC : 기울임(이텔릭체)
import numpy as np
import cv2

img = np.zeros((480, 640, 3), np.uint8)

SCALE = 1
COLOR = (255, 255, 255) # 색깔
THICKNESS = 1

cv2.putText(img, "Nado Simplex", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, SCALE, COLOR, THICKNESS)
# # 그릴 위치, 텍스트 내용, 시작위치, 폰트 종류, 크기, 색깔, 두께
cv2.putText(img, "Nado Plain", (20, 150), cv2.FONT_HERSHEY_PLAIN, SCALE, COLOR, THICKNESS)
cv2.putText(img, "Nado Script Simplex", (20, 250), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, SCALE, COLOR, THICKNESS)
cv2.putText(img, "Nado Triplex", (20, 350), cv2.FONT_HERSHEY_TRIPLEX, SCALE, COLOR, THICKNESS)
cv2.putText(img, "Nado Italic", (20, 450), cv2.FONT_HERSHEY_TRIPLEX | cv2.FONT_ITALIC, SCALE, COLOR, THICKNESS)


# 한글
# opencv는 한글지원을 제공하지 않기때문에 그냥 출력시 글자가 깨진다.
cv2.putText(img, "나도 코딩", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, SCALE, COLOR, THICKNESS)


# 한글 우회 방법
# PIL : python image library
from PIL import ImageFont, ImageDraw, Image
def myPutText(src, text, pos, font_size, font_color):
    img_pil = Image.fromarray(src)
    draw = ImageDraw.Draw(img_pil)
    font = ImageFont.truetype('fonts/gulim.ttc', font_size)
    draw.text(pos, text, font=font, fill=font_color)
    return np.array(img_pil) 

FONT_SIZE = 30
COLOR = (255, 255, 255)
img = myPutText(img, "나도 코딩", (20, 50), FONT_SIZE, COLOR)

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
