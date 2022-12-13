"""
05. 파일 저장
"""
# 이미지 저장
import cv2
img = cv2.imread("./sample/img.jpg", cv2.IMREAD_GRAYSCALE)
# cv2.imshow("img", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

cv2.imwrite("./sample/save.jpg", img)  # 저장에 성공하면 True반환
 
# 저장포맷(jpg, png)
cv2.imwrite("./sample/save.png", img)  # 저장에 성공하면 True반환


# 동영상 저장
cap = cv2.VideoCapture('./sample/video.mp4')

# 코덱정의
fourcc = cv2.VideoWriter_fourcc(*"DIVX")
# 프레임 크기, FPS
width = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))    # 정수값
height = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS) * 2 # 영상 속도 2배

out = cv2.VideoWriter("./sample/output_fast.avi", fourcc, fps, (width, height))
# 파일명, 코덱, 재생속도, 크기(width, height)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    out.write(frame)            # 영상 데이터만 저장. 소리 x
    cv2.imshow("video", frame)
    
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()   # 자원 해제
out.release()
cv2.destroyAllWindows()
