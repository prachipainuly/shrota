import cv2
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
    # mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
    mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
    # mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)


mp_holistic = mp.solutions.holistic
mp_drawing = mp.solutions.drawing_utils


def get_handpoints_from_singleframe(filename):
    """
        Function to extract x,y,z handpoints (21 each) for a single frame
        :param filename:
        :return:
    """
    # filename = "C:/Users/jenss/Desktop/ASL_alphabet/e.png"

    right_hand_coordinates_x = []
    right_hand_coordinates_y = []
    right_hand_coordinates_z = []

    cap = cv2.imread(filename)

    # cv2.imshow('ImageWindow', cap)

    with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
        print("Extracting handpoints....")
        ret = True
        if ret:
            # get handpoints by above function, store it into results
            frame, results = media_pipe_detect_hand_points(cap, holistic)
            print("Process complete!")
            if results:
                print(results)
                if results.right_hand_landmarks:
                    for res in results.right_hand_landmarks.landmark:
                        right_hand_coordinates_x.append(res.x)
                        right_hand_coordinates_y.append(res.y)
                        right_hand_coordinates_z.append(res.z)
            # draw the handpoints from landmarks
            draw_hand_points(cap, results)
            # cv2.imshow('ImageWindow', cap)

    # cv2.waitKey()
    cv2.destroyAllWindows()

    return [right_hand_coordinates_x, right_hand_coordinates_y, right_hand_coordinates_z]

# NOW WE WRITE TO CSV
#
# with open('C:/Users/jenss/Desktop/ASL_alphabet/e.csv', 'w') as f:
#     # create the csv writer
#     writer = csv.writer(f)
#
#     # write a row to the csv file
#     #for x in right_hand_coordinates_x:
#     writer.writerow(right_hand_coordinates_x)
#     writer.writerow("NOW Y")
#     #for x in right_hand_coordinates_y:
#     writer.writerow(right_hand_coordinates_y)
#     writer.writerow("NOW Z")
#     #for x in right_hand_coordinates_z:
#     writer.writerow(right_hand_coordinates_z)
