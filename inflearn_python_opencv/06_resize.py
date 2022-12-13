"""
06. 크기조정
"""
# 이미지
## 1. 고정크기 설정
import cv2
img = cv2.imread("./sample/img.jpg")
det = cv2.resize(img, (400, 500))   # width, height 고정크기

## 2. 비율 설정
det = cv2.resize(img, None, fx=0.5, fy=0.5)   # x, y 비율 정의(0.5배)


## 보간법
## 1. cv2.INTER_AREA : 크기 줄일 때 사용
## 2. cv2.INTER_CUBIC : 크기 늘릴 때 사용(속도 느림, 퀄리티 좋음)
## 3. cv2.INTER_LINEAR : 크기 늘릴 대 사용(기본값)

### 보간법을 적용하여 축소
det = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

### 보간법을 적용하여 확대
det = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)

cv2.imshow("img", img)
cv2.imshow("resize", det)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 동영상
cap = cv2.VideoCapture("./sample/video.mp4")
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    ## 1.고정크기 설정
    frame_resized = cv2.resize(frame, (400, 500))
    # 2. 비율 설정
    frame_resized = cv2.resize(frame, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
    cv2.imshow("video", frame_resized)

    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
