"""
12. 이미지 변형 - 원근
"""
import numpy as np
import cv2

# # 사다리꼴 이미지 펼치기
img = cv2.imread('./sample/newspaper.jpg')
width, height = 640, 240        # 가로크기 640, 세로크기 240으로 결과물 출력

src = np.array([[511, 352], [1008, 345], [1122, 584], [455, 594]], dtype=np.float32)    # input 4개 지점
dst = np.array([[0, 0], [width, 0], [width, height], [0, height]], dtype=np.float32)    # ouput 4개 지점
# 좌상, 우상, 우하, 좌하 시계방향으로 4개의 지점 정의

matrix = cv2.getPerspectiveTransform(src, dst)
result = cv2.warpPerspective(img, matrix, (width, height))

# 회전된 이미지 올바로 세우기
img = cv2.imread('./sample/poker.jpg')
width, height = 530, 710
src = np.array([[702, 143], [1133, 414], [726, 1007], [276, 700]], dtype=np.float32)
dst = np.array([[0, 0], [width, 0], [width, height], [0, height]], dtype=np.float32)    # ouput 4개 지점

matrix = cv2.getPerspectiveTransform(src, dst)
result = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("img", img)
cv2.imshow("result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
