import cv2
import os

test_path = r"C:\Users\19033\PycharmProjects\FaceRecogProject\test.jpg"

if not os.path.exists(test_path):
    print("test.jpg not found! Capture a new image.")
else:
    img = cv2.imread(test_path)
    if img is None:
        print("OpenCV cannot read test.jpg! Try saving it in a different format.")
    else:
        print("test.jpg loaded successfully!")
        cv2.imshow("Test Image", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
