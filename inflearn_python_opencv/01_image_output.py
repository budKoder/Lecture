"""
01. 이미지 출력

# 환경설정
prompt에 [pip install openv-python] 설치
"""
import cv2
print(cv2.__version__)
"""
OpenCV(Computer Vision)
: 다양한 영상(이미지)/동영상 처리에 사용되는 오픈소스 라이브러리
"""
# 1. 이미지 출력
img = cv2.imread("./sample/img.jpg") # 해당 경로의 파일 읽어오기
# cv2.imshow("img", img)              # img라는 이름의 창에 img를 표시
key = cv2.waitKey(0)                # 지정된 시간동안 사용자 key입력 대기(ms) (0 : 무한정 대기)
print(key)                          # 어떤 키 입력인지 확인(ascii)
cv2.destroyAllWindows()             # 모든 창 닫기

## 읽기 옵션
## 1. cv2.IMREAD_COLOR : 컬러 이미지. 투명 영역은 무시(기본값)
## 2. cv2.IMREAD_GRAYSCALE : 흑백 이미지
## 3. cv2.IMREAD_UNCHAGNED : 투명 영역까지 포함
img_color = cv2.imread("./sample/img.jpg", cv2.IMREAD_COLOR)
img_gray = cv2.imread("./sample/img.jpg", cv2.IMREAD_GRAYSCALE)
img_unchanged = cv2.imread("./sample/img.jpg", cv2.IMREAD_UNCHANGED)
cv2.imshow("img_color", img_color)
cv2.imshow("img_gray", img_gray)
cv2.imshow("img_unchanged", img_unchanged)
cv2.waitKey(0)
cv2.destroyAllWindows()

## Shape
## 이미지의 height, width, channel 정보
## channel = 3 : rgb 3가지를 사용한 이미지
print(img.shape)
