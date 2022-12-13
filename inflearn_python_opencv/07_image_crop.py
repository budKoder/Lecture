"""
7. 이미지 자르기
"""
# 1. 영역을 잘라서 새로운 윈도우(창)에 표시
import cv2
img = cv2.imread("./sample/img.jpg")
# img.shape = (390, 640, 3)

crop = img[100:200, 200:400] # 세로기준 100~200 / 가로기준 300~400

# 2. 영역을 잘라서 기준 윈도우에 표시
crop = img[100:200, 200:400]
img[100:200, 400:600] = crop
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
