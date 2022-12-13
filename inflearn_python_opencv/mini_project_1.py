# 미니 프로젝트 : 반자동 문서 스캐너
import numpy as np
import cv2
point_list = []
src_img = cv2.imread("./sample/poker.jpg")

COLOR = (255, 0, 255)
THICKNESS = 3
drawing = False # 선을 그릴지 여부. 지점을 하나 선택한 이후부터 그림


## 마우스 이벤트 등록
def mouse_handler(event, x, y, flags, param):
    global drawing
    dst_img = src_img.copy()

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True  # 선을 그리기 시작
        point_list.append((x,y))
    
    if drawing:
        previous_point = None   # 직선의 시작점
        for point in point_list:
            cv2.circle(dst_img, point, 15, COLOR, cv2.FILLED)
            
            if previous_point:
                cv2.line(dst_img, previous_point, point, COLOR, THICKNESS, cv2.LINE_AA)
            
            previous_point = point

        next_point = (x, y)
        if len(point_list) == 4:
            show_result()   # 결과 출력
            next_point = point_list[0]  # 첫번째 클릭한 지점
        cv2.line(dst_img, next_point, point, COLOR, THICKNESS, cv2.LINE_AA)

    cv2.imshow("img", dst_img)


def show_result():
    width, height = 530, 710
    src = np.float32(point_list)
    dst = np.array([[0, 0], [width, 0], [width, height], [0, height]], dtype=np.float32)    # ouput 4개 지점

    matrix = cv2.getPerspectiveTransform(src, dst)
    result = cv2.warpPerspective(src_img, matrix, (width, height))
    
    cv2.imshow("result", result)


cv2.namedWindow("img")
cv2.setMouseCallback("img", mouse_handler)
cv2.imshow("img", src_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
