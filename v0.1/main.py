import cv2

cv2.namedWindow("Camera Feed", cv2.WINDOW_NORMAL)

cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)  # OBS VirtualCam index

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    status_text = "Face detected" if len(faces) > 0 else "No face detected"

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.putText(frame, status_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 0, 255), 2, cv2.LINE_AA)

    # Get current window size
    win_x, win_y, win_w, win_h = cv2.getWindowImageRect("Camera Feed")

    # Resize frame to window size
    frame_resized = cv2.resize(frame, (win_w, win_h))

    cv2.imshow("Camera Feed", frame_resized)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

