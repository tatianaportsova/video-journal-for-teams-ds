"""
[?? To add ??]
"""

# We Import the necessary packages needed
import cv2
import numpy as np
import dlib

cap = cv2.VideoCapture(0)  # 'ALPACAVID-r7tjBJgdj.mp4'
# We initialise detector of dlib
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("./models/dlib_shape_predictor_68_face_landmarks.dat")

# Get frames:
total_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
frame_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print(f"Frame width x height: {frame_width} x {frame_height}")

# Start the main program
while True:
    _, frame = cap.read()

    # We actually Convert to grayscale conversion
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    for face in faces:
        # The face landmarks code begins from here
        x1 = face.left()
        y1 = face.top()
        w = face.right()
        h = face.bottom()
        # Then we can also do
        # cv2.rectangle function (frame, (x1, y1), (x2, y2), (0, 255, 0), 3)
        cv2.rectangle(frame, (x1, y1), (w, h), (0, 255, 0), 3)
        cv2.rectangle(frame,
                      (int(0.20*frame_width), int(0.20*frame_height)),
                      (int(frame_width - 0.20*frame_width), int(frame_height - 0.20*frame_height)),
                      (0, 0, 255),
                      3)

        landmarks = predictor(gray, face)
        # We are then accesing the landmark points
        for n in range(0, 68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            cv2.circle(frame, (x, y), 2, (255, 255, 0), -1)
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break # press esc the frame is destroyed