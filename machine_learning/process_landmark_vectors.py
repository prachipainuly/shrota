from dtw_test import compare_two_sequences

def get_landmark_sequence_similarity(gesture1_vector, gesture2_vector):
    left_hand_similarity = 0
    right_hand_similarity = 0

    for i in range(21):
        # get the time series for each landmark: We start with x
        left_hand_similarity += compare_two_sequences(gesture1_vector[0][0][i::21], gesture2_vector[0][0][i::21])
        right_hand_similarity += compare_two_sequences(gesture1_vector[1][0][i::21], gesture2_vector[1][0][i::21])

        # now y
        left_hand_similarity += compare_two_sequences(gesture1_vector[0][1][i::21], gesture2_vector[0][1][i::21])
        right_hand_similarity += compare_two_sequences(gesture1_vector[1][1][i::21], gesture2_vector[1][1][i::21])
        # now z
        left_hand_similarity += compare_two_sequences(gesture1_vector[0][2][i::21], gesture2_vector[0][2][i::21])
        right_hand_similarity += compare_two_sequences(gesture1_vector[1][2][i::21], gesture2_vector[1][2][i::21])

    return [left_hand_similarity, right_hand_similarity]
