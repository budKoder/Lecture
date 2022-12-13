"""
11. 이미지 변형 - 흐림
"""
import cv2
img = cv2.imread("./sample/img.jpg")

# 가우시안 블러(이미지를 흐리게 & 노이즈 제거)
## 1. 커널사이즈 변화에 따른 흐림

# kernel size : [3,3], [5,5], [7,7] 에 대해 우수한 성능을 보이므로 이 중 골라서 사용
# kernel size가 클수록 흐림효과 up
kernel_3 = cv2.GaussianBlur(img, (3,3), 0)
kernel_5 = cv2.GaussianBlur(img, (5,5), 0)
kernel_7 = cv2.GaussianBlur(img, (7,7), 0)

## 2. 표준편차 변화에 따른 흐림
# sigmaX : 가우시안 커널의 x방향의 표준편차
sigma_1 = cv2.GaussianBlur(img, (0,0), 1)
sigma_2 = cv2.GaussianBlur(img, (0,0), 2)
sigma_3 = cv2.GaussianBlur(img, (0,0), 3)


cv2.imshow("img", img)

cv2.imshow("kernel_3", kernel_3)
cv2.imshow("kernel_5", kernel_5)
cv2.imshow("kernel_7", kernel_7)

cv2.imshow("sigma_1", sigma_3)
cv2.imshow("sigma_2", sigma_2)
cv2.imshow("sigma_3", sigma_3)
cv2.waitKey(0)
cv2.destroyAllWindows()
