"""
9. 이미지 회전
"""
import cv2
img = cv2.imread("./sample/img.jpg")

# 시계방향 90도 회전
rotate_90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

# 180도 회전
rotate_180 = cv2.rotate(img, cv2.ROTATE_180)

# 시계반대방향 90도 회전
rotate_270 = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)    

cv2.imshow("img", img)
cv2.imshow("rotate", rotate_270)
cv2.waitKey(0)
cv2.destroyAllWindows()
