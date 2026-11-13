import sys
import time
from pathlib import Path

import cv2 as cv

# creating video capture object
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    sys.exit()

# getting the width and height of the frame
frame_width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

# used to set the output path to save the video
output_path = Path(__file__).parent / "output.mp4"

fourcc = cv.VideoWriter_fourcc(*"mp4v")
out = cv.VideoWriter(str(output_path), fourcc, 20.0, (frame_width, frame_height))

# used to record the time when processed last frame
prev_frame_time = time.time()

while cap.isOpened():
    # Capturing frame by frame
    ret, frame = cap.read()

    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # used to record the time when processed current frame
    new_frame_time = time.time()

    # calculating the fps
    time_diff = new_frame_time - prev_frame_time
    fps = int(1 / time_diff) if time_diff > 0 else 0
    prev_frame_time = new_frame_time

    # show the fps on the frame
    cv.putText(
        frame,
        f"FPS: {fps}",
        (10, 40),
        cv.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2,
        cv.LINE_AA,
    )

    # write the frame to the output video file
    out.write(frame)

    # display the resulting frame
    cv.imshow("frame", frame)
    if cv.waitKey(1) == ord("q"):
        break


# When everything done, release the capture
cap.release()
out.release()
cv.destroyAllWindows()
