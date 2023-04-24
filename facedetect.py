import cv2
from cvzone.FaceDetectionModule import FaceDetector

cap = cv2.VideoCapture(0)
detecter = FaceDetector()

while True:
    ret,frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame,bboxs = detecter.findFaces(frame)
    
    cv2.imshow('Face Detector', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
