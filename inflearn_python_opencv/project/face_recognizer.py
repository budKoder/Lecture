# 프로젝트 : 얼굴을 인식하여 캐릭터 씌우기
## Face Detection vs Face Recognition
### Face Detection : 얼굴을 찾는 것
### Face Recognition : 누구의 얼굴인지 알아내는 것
import cv2
# 패키지 설치 : pip install mediapipe
import mediapipe as mp

def overlay(image, x, y, w, h, overlay_image): # 대상이미지(3채널 이미지), x, y, w, h, 덮어씌울 이미지(4채널 이미지)
  alpha = overlay_image[:, :, 3] # BGRA
  mask_image = alpha/255 # alpha(0~255) / mask(0~1) 1은 불투명, 0은 투명
  # [255, 255] > [1, 1]
  # [255, 0] > [1, 0]
  
  # 1-mask_image
  # [0, 0]
  # [0, 1]
  for c in range(0, 3): # Channel BGR
    image[y-h:y+h, x-w:x+w, c] = (overlay_image[:, :, c] * mask_image) + (image[y-h:y+h, x-w:x+w, c] * (1-mask_image))


# 얼굴을 찾고, 찾은 얼굴에 표시를 해주기 위한 변수 정의
mp_face_detection = mp.solutions.face_detection # 얼굴 검출을 위해서 face detection 모듈 사용
mp_drawing = mp.solutions.drawing_utils         # 얼굴의 특징을 그리기 위한 drawing_utils 모듈 사용

# 동영상 파일 열기
cap = cv2.VideoCapture("./sample/face_video.mp4")
# 이미지 불러오기
image_right_eye = cv2.imread("./sample/right_eye.png", cv2.IMREAD_UNCHANGED)
image_left_eye = cv2.imread("./sample/left_eye.png", cv2.IMREAD_UNCHANGED)
image_nose_tip = cv2.imread("./sample/nose_tip.png", cv2.IMREAD_UNCHANGED)
# with : 별도의 close문 필요 없이 with문 탈출 후 자동으로 close
with mp_face_detection.FaceDetection(
    # model_selection : face_detection이라는 객체를 만드는데 사용할 모델 index(0 : 근거리(2m이내) / 1: 5m 이내)
    # min_detection_confidence : 어느정도 확률 이상일 때 얼굴이라고 볼 것인지(threshold와 비슷) (0~1사이)
    model_selection=0, min_detection_confidence=0.7) as face_detection:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
        break

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = face_detection.process(image)

    # Draw the face detection annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.detections:
      for detection in results.detections:
        # 6개의 특징(좌표)을 뽑아낸다. 오른쪽눈, 왼쪽눈, 코끝, 입중심, 오른쪽귀, 왼쪽귀(귀구슬점. 이주)
        # mp_drawing.draw_detection(image, detection)
        # print(detection)

        # 특정위치 가져오기
        keypoint = detection.location_data.relative_keypoints
        right_eye = keypoint[0] # 오른쪽 눈(0~1사이의 값)
        left_eye = keypoint[1]  # 왼쪽 눈
        nose_tip = keypoint[2]  # 코끝

        h, w, _ = image.shape   # height, width, channel : 이미지로부터 세로, 가로 크기 가져옴
        right_eye = (int(right_eye.x * w)-20, int(right_eye.y * h)-100) # 이미지 내에서 실제좌표(x,y)
        left_eye = (int(left_eye.x * w)+20, int(left_eye.y * h)-100) # 이미지 내에서 실제좌표(x,y)
        nose_tip = (int(nose_tip.x * w), int(nose_tip.y * h)) 
        
        # # 양 눈에 동그라미 그리기
        # cv2.circle(image, right_eye, 50, (255, 0, 0), 10, cv2.LINE_AA)
        # cv2.circle(image, left_eye, 50, (0, 255, 0), 10, cv2.LINE_AA)
        # # 코끝에 동그라미 그리기
        # cv2.circle(image, nose_tip, 70, (0, 255, 255), 10, cv2.LINE_AA)

        # 각 특징에 이미지 넣기
        # image[right_eye[1]-50 : right_eye[1]+50, right_eye[0]-50:right_eye[0]+50] = image_right_eye
        # image[left_eye[1]-50 : left_eye[1]+50, left_eye[0]-50 : left_eye[0]+50] = image_left_eye
        # image[nose_tip[1]-50 : nose_tip[1]+50, nose_tip[0]-150 : nose_tip[0]+150] = image_nose_tip

        overlay(image, *right_eye, 50, 50, image_right_eye)
        overlay(image, *left_eye, 50, 50, image_left_eye)
        overlay(image, *nose_tip, 150, 50, image_nose_tip)
        
    
    cv2.imshow('MediaPipe Face Detection', cv2.resize(image, None, fx=0.5, fy=0.5))

    if cv2.waitKey(1) == ord("q"):
      break
cap.release()
cv2.destroyAllWindows()