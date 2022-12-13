"""
13. 이미지 변형(이진화)
이진화 : 특정 값을 기준으로 흰색과 검은색만 가지는 binary 이미지로 바꾸는 것
"""
import cv2
img = cv2.imread('./sample/book.jpg', cv2.IMREAD_GRAYSCALE)

# Threshold
##  threshold : threshold의 값을 기준으로 판단
ret, binary = cv2.threshold(img, 127, 255, 0)
## 픽셀값이 127보다 크면 255(흰색), 작으면 0(검은색)


# Trackbar(값 변화에 따른 변형 확인)
def empty(pos):
    # print(pos)
    pass

name = "Trackbar"
cv2.namedWindow(name)
cv2.createTrackbar("threshold", name, 127, 255, empty) # 바의 이름, 창의 이름, 초기값, 최대값, 이벤트처리

while True:
    thres = cv2.getTrackbarPos("threshold", name)       # 바의 이름, 창의 이름
    ret, binary = cv2.threshold(img, thres, 255, 0)

    if not ret:
        break
    cv2.imshow(name, binary)
    if cv2.waitKey(1) == ord('q'):
        break

# 그림판에서 제작한 이미지로 확인
img = cv2.imread('./sample/threshold.png', cv2.IMREAD_GRAYSCALE)


# threshold : threshold의 값을 기준으로 판단
ret, binary = cv2.threshold(img, 127, 255, 0)
# 픽셀값이 127보다 크면 255(흰색), 작으면 0(검은색)


# Trackbar(값 변화에 따른 변형 확인)
def empty(pos):
    # print(pos)
    pass

name = "Trackbar"
cv2.namedWindow(name)
cv2.createTrackbar("threshold", name, 127, 255, empty) # 바의 이름, 창의 이름, 초기값, 최대값, 이벤트처리

while True:
    thres = cv2.getTrackbarPos("threshold", name)       # 바의 이름, 창의 이름
    ret, binary = cv2.threshold(img, thres, 255, 0)

    if not ret:
        break
    cv2.imshow("img", img)
    cv2.imshow(name, binary)
    if cv2.waitKey(1) == ord('q'):
        break


img = cv2.imread('./sample/threshold.png', cv2.IMREAD_GRAYSCALE)

ret, binary1 = cv2.threshold(img, 0, 255, 0)        # 진한회색, 밝은회색, 흰색 > 흰색
ret, binary2 = cv2.threshold(img, 127, 255, 0)      # 밝은회색, 흰색 > 흰색
ret, binary3 = cv2.threshold(img, 195, 255, 0)      # 흰색 > 흰색

cv2.imshow("binary1", binary1)
cv2.imshow("binary2", binary2)
cv2.imshow("binary3", binary3)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Adaptive Threshold
# threshold : 이미지 전체 / Adaptive threshold : 이미지를 작은 영역으로 나누어 임계치 적용
def empty(pos):
    # print(pos)
    pass

img = cv2.imread('./sample/book.jpg', cv2.IMREAD_GRAYSCALE)

name = "Trackbar"
cv2.namedWindow(name)

cv2.createTrackbar("block_size", name, 25, 100, empty)  # block size는 홀수만 가능. 1보다 큰 값
cv2.createTrackbar("c", name, 3, 10, empty)             # 일반적으로 양수 값을 사용


while True:
    block_size = cv2.getTrackbarPos("block_size", name)
    c = cv2.getTrackbarPos("c", name)

    if block_size <= 1:
        block_size = 3
    if block_size % 2 == 0:
        block_size += 1

    binary = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, block_size, c)

    cv2.imshow(name, binary)
    if cv2.waitKey(1) == ord('q'):
        break


# 오츠 알고리즘
# Bimodal image에 사용하기 적합. 최적의 임계치를 자동으로 발견
img = cv2.imread("./sample/book.jpg", cv2.IMREAD_GRAYSCALE)

ret, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
ret, ostu = cv2.threshold(img, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) # 두번째 인자는 값이 있더라도 ostu가 최적값을 찾으면 그 값을 사용
print('ostu threshold', ret)

cv2.imshow("img", img)
cv2.imshow("binary", binary)
cv2.imshow("ostu", ostu)
cv2.waitKey(0)
cv2.destroyAllWindows()