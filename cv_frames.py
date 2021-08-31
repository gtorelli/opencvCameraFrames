# Run> python zoom.py 500 5
import cv2
import sys
import time
capture = cv2.VideoCapture(0)
count = 0
i = 0

while(True):

    ret, frame = capture.read()
    scale_percent = int(sys.argv[1])
    width = int(frame.shape[1] * scale_percent / 100)
    height = int(frame.shape[0] * scale_percent / 100)

    dsize = (width, height)

    frame = cv2.resize(frame, dsize)
    cv2.imshow('video', frame)

    cv2.imwrite('Frame-{num:0005d}.jpg'.format(num=i), frame)
    i += 1
    time.sleep(int(sys.argv[2]))

    if cv2.waitKey(1) == 27:
        break

capture.release()
cv2.destroyAllWindows()
