"""
10. 이미지 변형 - 흑백
"""
import cv2
# 이미지를 흑백으로 읽음
img = cv2.imread('./sample/img.jpg', cv2.IMREAD_GRAYSCALE)

# 불러온 이미지를 흑백으로 변경
img = cv2.imread('./sample/img.jpg')
dst = cv2.cvtColor(img ,cv2.COLOR_BGR2GRAY)

cv2.imshow("img", img)
cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
