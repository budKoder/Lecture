"""
19. 퀴즈
"""
# Q. Opencv를 이용하여 가로로 촬영된 영상을 세로로 회전하는 프로그램을 작성하시오.
## 조건
### 1. 회전 : 시계 반대방향으로 회전
### 2. 속도 : 원본 4배
### 3. 출력 : city_output.avi(코덱 DIVX)

### 원본파일명 : city.mp4
import cv2

cap = cv2.VideoCapture("./sample/city.mp4")

fourcc = cv2.VideoWriter_fourcc(*"DIVX")
width = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

out = cv2.VideoWriter("./sample/city_output.avi", fourcc, fps*4, (height, width))
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    rotate = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
    out.write(rotate)

cap.release()
out.release()
cv2.destroyAllWindows()
