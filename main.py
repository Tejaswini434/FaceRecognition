import threading
import cv2
from deepface import DeepFace

camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

frame_counter = 0

reference_image = cv2.imread(r"C:\Users\19033\PycharmProjects\FaceRecogProject\image1.jpg")

if reference_image is None:
    print("Error:Image not found or cannot be read!")
    exit()

is_match = False


def verify_face(snapshot):
    global is_match
    try:
        result = DeepFace.verify(snapshot, reference_image.copy())
        is_match = result.get("verified", False)
    except Exception as error:
        print(f"Error in face verification: {error}")
        is_match = False


while True:
    success, frame_capture = camera.read()

    if success:
        if frame_counter % 30 == 0:
            threading.Thread(target=verify_face, args=(frame_capture.copy(),)).start()

        frame_counter += 1

        display_text = "MATCH!" if is_match else "NO MATCH!"
        text_color = (0, 255, 0) if is_match else (0, 0, 255)

        cv2.putText(frame_capture, display_text, (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, text_color, 3)
        cv2.imshow('camera', frame_capture)

    if cv2.waitKey(1) == ord('x'):
        break

camera.release()
cv2.destroyAllWindows()
