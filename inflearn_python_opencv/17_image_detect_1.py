"""
17. 이미지 검출 - 경계선
"""
# 경계선 : 갑자기 픽셀 색깔이 변하는 지점
import cv2

# Canny Edge Detection(성능이 좋고, noise에 민감하지 않음)
img = cv2.imread("./sample/snowman.png")
canny = cv2.Canny(img, 150, 200)    # 대상이미지, min(하위임계값), max(상위임계값). 픽셀의 변화가 max보다 크면 경계선으로 인식. min보다 작으면 경계값으로 인식 x
# cv2.imshow("img", img)
# cv2.imshow("canny", canny)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# Trackbar
def empty(pos):
    pass

img = cv2.imread("./sample/snowman.png")

name = "Trackbar"
cv2.namedWindow(name)
cv2.createTrackbar("threshold1", name, 0, 255, empty)
cv2.createTrackbar("threshold2", name, 0, 255, empty)

while True:
    threshold1 = cv2.getTrackbarPos("threshold1", name)
    threshold2 = cv2.getTrackbarPos("threshold2", name)

    canny = cv2.Canny(img, threshold1, threshold2)

    cv2.imshow("img", img)
    cv2.imshow(name, canny)

    if cv2.waitKey(1) == ord('q'):
        break
