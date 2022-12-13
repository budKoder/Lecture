"""
02. 동영상 출력
"""
# 동영상 파일 출력
import cv2
cap = cv2.VideoCapture('./sample/video.mp4')
while cap.isOpened():       # 동영상 파일이 올바로 열렸는지?
    ret, frame = cap.read() # ret: 성공여부, frame : 받아온 이미지 frame
    if not ret:             # ret = False : 더이상 가져올 프레임이 없는 경우
        print("더 이상 가져올 프레임이 없어요.")
        break
    cv2.imshow("video", frame)

    if cv2.waitKey(25) == ord("q"):
        print("사용자 입력에 의해 종료합니다.")
        break
cap.release()               # 읽어온 자원 해제
cv2.destroyAllWindows()

# 카메라 출력
cap = cv2.VideoCapture(0)   # 0번째 카메라 장치
if not cap.isOpened():      # 카메라가 잘 열리지 않은 경우
    exit()                  # 프로그램 종료
while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("camera", frame)

    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
