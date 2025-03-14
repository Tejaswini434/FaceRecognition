import cv2
import os

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Camera not working!")
        break

    cv2.imshow("Capture Image", frame)

    key = cv2.waitKey(1)
    if key == ord('s'):
        img_path = r"C:\Users\19033\PycharmProjects\FaceRecogProject\test.jpg"
        cv2.imwrite(img_path, frame)
        print("Image saved as test.jpg!")
        break
    elif key == ord('q'):
        print("Image capture cancelled!")
        break

cap.release()
cv2.destroyAllWindows()
