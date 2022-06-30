from Machine_learning.open_video_and_display import get_landmarks_from_video

# Absolute file paths to different videos displaying the word 'book'
file_prefix = 'C:/Users/jenss/PycharmProjects/shrota/start_kit/raw_videos/'
filepath_book = ['69241.mp4',  '07099.mp4', '07074.mp4', '07070.mp4',
                 '07069.mp4', '07068.mp4']
for i in range(len(filepath_book)):
    filepath_book[i] = file_prefix + filepath_book[i]

# list in which we will store the landmark points for every of the analyzed videos
results = []
for file in filepath_book:
    results.append(get_landmarks_from_video(file))

# Now results contains xyz coordinates for set of landmarks for gesture

# TODO: Feed the data to machine learning model (maybe Tensor Flow) to later recognize gestures