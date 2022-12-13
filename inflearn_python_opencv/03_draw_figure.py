"""
03. 도형그리기
"""
# 빈 스케치북 그리기
import cv2
import numpy as np

# 세로 480 * 가로 640 * 3 Channel(RGB) 에 해당 하는 스케치북 만들기
img = np.zeros((480, 640, 3), dtype=np.uint8)   # 480 * 640 * 3의 공간을 만들고 0으로 채우기
# img[:] = [255, 255, 255]  # 흰색으로 채우기 (BGR)


# 일부 영역 색칠
img[100:200, 200:300] = [255,255,255]   # [세로영역, 가로영역]


# 직선
## 직선의 종류
## 1. cv2.LINE_4 : 상하좌우 4방향으로 연결된 선
## 2. cv2.LINE_8 : 대각선을 포함한 8방향으로 연결된 선(기본값)
## 3. cv2.LINE_AA : 부드러운 선(anti-aliasing)
COLOR = (0, 255, 255)   # 선색(BGR)
THICKNESS = 3           # 선두께
cv2.line(img, (50,100), (400, 50), COLOR, THICKNESS, cv2.LINE_8)
cv2.line(img, (50,200), (400, 150), COLOR, THICKNESS, cv2.LINE_4)
cv2.line(img, (50,300), (400, 250), COLOR, THICKNESS, cv2.LINE_AA)
# 그릴위치, 시작점, 끝점, 색깔, 두께, 선종류


# 원
COLOR = (255, 255, 0)   # 선색(BGR)
THICKNESS = 10          # 선두께
RADIUS = 50             # 반지름 
cv2.circle(img, (200, 100), RADIUS, COLOR, THICKNESS, cv2.LINE_AA)      # 속이 빈 원
cv2.circle(img, (400, 100), RADIUS, COLOR, cv2.FILLED, cv2.LINE_AA)     # 속이 찬 원
# 그릴위치, 원의 중심점, 반지름, 색깔, 두께, 선종류


# 사각형
COLOR = (0, 255, 0)     # 선색(BGR)
THICKNESS = 3           # 선두께
cv2.rectangle(img, (100, 100), (200, 200), COLOR, THICKNESS, cv2.LINE_AA)   # 속이 빈 사각형
cv2.rectangle(img, (300, 100), (400, 300), COLOR, cv2.FILLED, cv2.LINE_AA)  # 속이 빈 사각형
# 그릴위치, 왼쪽 위 좌표, 오른쪽 아래 좌표, 색깔, 두께, 선


# 다각형
COLOR = (0, 0, 255)     # 선색(BGR)
THICKNESS = 3           # 선두께
pts1 = np.array([[100, 100], [200, 100], [100, 200]])   # 내부 리스트는 다각형의 각 꼭짓점
pts2 = np.array([[200, 100], [300, 100], [300, 200]])
pts3 = np.array([[[100, 300], [200, 300], [100, 400]], [[200, 300], [300, 300], [300, 400]]])
cv2.polylines(img, [pts1], True, COLOR, THICKNESS, cv2.LINE_AA)
cv2.polylines(img, [pts2], True, COLOR, THICKNESS, cv2.LINE_AA)
cv2.polylines(img, [pts1, pts2], True, COLOR, THICKNESS, cv2.LINE_AA)   # 속이 빈 다각형
# 그릴위치, 그릴 좌표, 닫힘 여부, 색깔, 두께, 선
cv2.fillPoly(img, pts3, COLOR, cv2.LINE_AA)
# 그릴위치, 그릴 좌표, 색깔, 선


cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

