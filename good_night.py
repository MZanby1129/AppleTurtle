import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

while True:
	_, frame = cap.read()
	cv2.imshow("Face.Mesh",frame)
	if cv2.waitKey(1) & 0xFF ==ord("q"):
		break

cap.release()
cv2.destroyAllWindows()

