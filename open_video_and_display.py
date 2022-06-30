import cv2
import numpy as np
import mediapipe as mp

# use open cv for hand point retection: results will contain a set of landmarks with
# xyz coordinates for hand, pose and face points in the analyzed frame
def media_pipe_detect_hand_points(image, model):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image.flags.writeable = False
    results = model.process(image)
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    return image, results

# draw the landmarks detected by mediapipe in the image object
# by choosing CONNECTIONS lines are drawn between these points
def draw_hand_points(image, results):
    mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
    mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)


mp_holistic = mp.solutions.holistic
mp_drawing = mp.solutions.drawing_utils

def get_landmarks_from_video(filepath):
    # setup media pipe models for detection and drawing


    # open video with opencv
    cap = cv2.VideoCapture(filepath)


    pose_coordinates = []
    left_hand_coordinates = []
    right_hand_coordinates = []

    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print("Number of frames:")
    print(length)

    if (cap.isOpened() == False):
        print ("Error: Could not open video. Check file path")
    with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
        while (cap.isOpened()):
            ret, frame = cap.read()

            # DETECTION BY MODEL:
            if ret:
                # get handpoints by above function, store it into results
                frame, results = media_pipe_detect_hand_points(frame, holistic)
                # draw the handpoints from landmarks
                draw_hand_points(frame, results)

                # add the handpoints to lists which we can lateron return
                # if hand was not in picture there will be no element (so use if)
                if results.pose_landmarks:
                    # pose has 33 points with xyz for each point
                    for res in results.pose_landmarks.landmark:
                        pose_coordinates.append(res.x)
                        pose_coordinates.append(res.y)
                        pose_coordinates.append(res.z)
                if results.left_hand_landmarks:
                    # left hand has 21 points with xyz for each point
                    for res in results.left_hand_landmarks.landmark:
                        left_hand_coordinates.append(res.x)
                        left_hand_coordinates.append(res.y)
                        left_hand_coordinates.append(res.z)
                if results.right_hand_landmarks:
                    # right hand has (also) 21 points with xyz for each point
                    for res in results.right_hand_landmarks.landmark:
                        right_hand_coordinates.append(res.x)
                        right_hand_coordinates.append(res.y)
                        right_hand_coordinates.append(res.z)

            if ret:
                # Display video on screen
                cv2.imshow('Frame', frame)
                # EXIT BY PRESSING Q
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break
            else:
                break

        cap.release()

        cv2.destroyAllWindows()
    return [pose_coordinates, left_hand_coordinates, right_hand_coordinates]