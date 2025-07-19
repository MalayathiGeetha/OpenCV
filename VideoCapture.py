import cv2

cap = cv2.VideoCapture(0)  # 0 = default webcam

while True:
    ret, frame = cap.read()
    if ret:
        frame = cv2.resize(frame, (600, 500))
        cv2.imshow("Live Webcam", frame)

        # Press 'p' to stop
        if cv2.waitKey(30) & 0xFF == ord('p'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
