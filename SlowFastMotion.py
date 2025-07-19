import cv2

cap = cv2.VideoCapture("/home/rguktrkvalley/Desktop/Movies/songs/swathi reddy.mp4")  # 0 = default webcam

while True:
    ret, frame = cap.read()
    if ret:
        frame = cv2.resize(frame, (600, 500))
        cv2.imshow("Live Webcam", frame)

        # Press 'p' to stop  //more val of waitKeyleads to slow motion
        if cv2.waitKey(10) & 0xFF == ord('p'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
