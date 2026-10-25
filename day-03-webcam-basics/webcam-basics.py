import sys
import time

import cv2 as cv

# creating video capture object
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    sys.exit()

# used to record the time when processed last frame
prev_frame_time = 0

# used to record the time when processed current frame
new_frame_time = 0

while cap.isOpened():
    # Capturing frame by frame
    ret, frame = cap.read()

    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    new_frame_time = time.time()

    # Calculating the fps

    # fps will be number of frame processed in given time frame
    # since their will be most of time error of 0.001 second
    # we will be subtracting it to get more accurate result
    fps = 1 / (new_frame_time - prev_frame_time)
    prev_frame_time = new_frame_time

    # Converting the fps to integer
    fps = int(fps)

    # converting the fps to string so that we can display it on frame
    # by using putText function
    fps = f"FPS: {fps}"

    # putting the FPS count on the frame
    cv.putText(
        gray, fps, (7, 40), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3, cv.LINE_AA
    )

    # Display the resulting frame
    cv.imshow("frame", gray)
    if cv.waitKey(1) == ord("q"):
        break


# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
