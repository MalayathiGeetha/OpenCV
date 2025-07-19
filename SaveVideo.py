import cv2

cap = cv2.VideoCapture(0)

# Get actual width and height from the capture
frame_width = int(cap.get(3))  # CAP_PROP_FRAME_WIDTH
frame_height = int(cap.get(4)) # CAP_PROP_FRAME_HEIGHT

f = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("/home/rguktrkvalley/Desktop/demo.mp4", f, 20.0, (frame_width, frame_height))

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        frame = cv2.flip(frame, 1)
        out.write(frame)
        cv2.imshow("Live Webcam", frame)

        if cv2.waitKey(25) & 0xFF == ord('p'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
