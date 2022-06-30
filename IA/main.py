# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# import necessary packages for hand gesture recognition project using Python OpenCV

import cv2
import numpy as np
import mediapipe as mp
import tensorflow as tf
#error messages
VIDEO_DEVICE_EXCEPTION="Could not open video device"
RECORD_EXCEPTION="Could not Record video"
#size of the video
PLAYER_FRAME_WIDITH=1000
PLAYER_FRAME_HIGHT=1000
MAX_HAND_NUM=2
MIN_DETECTION_CONFIDENCE=0.7


# initialize mediapipe
MIN_DETECTION_CONFIDENCE=0.8
MIN_TRACKING_CONFIDENCE=0.8
POINT_COLOR=(250,0,0)
JOINT_COLOR=(0,0,250)
MP_DROWING=mp.solutions.drawing_utils
MP_HANDS=mp.solutions.hands

# Initialize the webcam for Hand Gesture Recognition Python project
cap = cv2.VideoCapture(1)
if not cap.isOpened():
  raise Exception("Could not open video device")
# set widow size
cap.set(cv2.CAP_PROP_FRAME_WIDTH, PLAYER_FRAME_WIDITH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, PLAYER_FRAME_HIGHT)
with MP_HANDS.Hands(min_detection_confidence=MIN_DETECTION_CONFIDENCE,min_tracking_confidence=MIN_TRACKING_CONFIDENCE,max_num_hands=MAX_HAND_NUM)as HANDS:
    while cap.isOpened():
  # Read each frame from the webcam
        Recording, frame = cap.read()
        if Recording==False:
            raise Exception("Could not Record video")
  # Flip the frame vertically
        frame = cv2.flip(frame, 1)
  #change the frame from BGR-color code to RGB image
        image=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
  #set flage
        image.flags.writeable=False
  #Detections
        results=HANDS.process(image)
  #set flage to true
        image.flags.writeable=True
  #RGB TO BGR
        image=cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
        if results.multi_hand_landmarks:
            for num , hand in enumerate(results.multi_hand_landmarks):
                MP_DROWING.draw_landmarks(image,hand,MP_HANDS.HAND_CONNECTIONS,
                                          MP_DROWING.DrawingSpec(color=JOINT_COLOR,thickness=1, circle_radius=5),
                                          MP_DROWING.DrawingSpec(color=POINT_COLOR,thickness=1, circle_radius=10))





# Show the final output
        cv2.imshow("Output", image)
        if cv2.waitKey(1) == ord('q'):
            break

# release the webcam and destroy all active windowsa
cap.release()
cv2.destroyAllWindows()

