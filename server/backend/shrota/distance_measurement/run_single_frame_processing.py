import math

from Machine_learning.read_single_frames import get_handpoints_from_singleframe

def calculate_distance_from_two_frames(index1, index2, results):
    diff1 = 0
    for i in range(20):
        ## for each landmark_point we compare difference:
        diff1 += math.sqrt((results[index1][0][i + 1] - results[index2][0][i + 1]) ** 2 +
                           (results[index1][1][i + 1] - results[index2][1][i + 1]) ** 2 +
                           (results[index1][2][i + 1] - results[index2][2][i + 1]) ** 2)
    return diff1




datapath = "C:/Users/jenss/Desktop/ASL_alphabet/"

dataset = ["a", "a1", "b", "b1", "c3", "c1", "d3", "d1", "e", "e3"]

for i in range(len(dataset)):
    dataset[i] = datapath + dataset[i] + ".png"

results = []
## This loop will process all images in dataset and store the landmark points
## in the results list
for datapoint in dataset:
    results.append (get_handpoints_from_singleframe(datapoint))

print("done processing the frames. Now we want to normalize to (a) handpoint 0 of wrist and (b) size of hand")

print(results[0][0])
print(results[0][1])
print(results[0][2])

for i in range(len(dataset)):
    ## This will give us the vector of the first handpoint with index 0 (wrist)
    x_zero = results[i][0][0]
    y_zero = results[i][1][0]
    z_zero = results[i][2][0]


    ## Now we measure the size of the hand! This will be done by calculating distance from
    ## landmark 0 to landmark 5
    handsize_reference = math.sqrt( (x_zero - results[i][0][5])**2 + (y_zero - results[i][1][5])**2 + (z_zero - results[i][2][5])**2 )
    print(handsize_reference)

    ## Now based on the handsize_reference we can normalize landmarks to hand size

    for j in range(20):
        results[i][0][j+1] = (results[i][0][j+1] - x_zero) / handsize_reference
        results[i][1][j + 1] = (results[i][1][j + 1] - y_zero) / handsize_reference
        results[i][2][j + 1] = (results[i][2][j + 1] - z_zero) / handsize_reference


## Now we have everything normalized!
## Time for some distance measurements and comparisons!



print("First comparison betwenn a und a1 (should be similar):")
print(calculate_distance_from_two_frames(0, 1, results))

print("First comparison betwenn b und b1 (should be similar):")
print(calculate_distance_from_two_frames(2, 3, results))

print("First comparison betwenn c und c1 (should be similar):")
print(calculate_distance_from_two_frames(4, 5, results))

print("First comparison betwenn d und d1 (should be similar):")
print(calculate_distance_from_two_frames(6, 7, results))

print("First comparison betwenn e und e1 (should be similar):")
print(calculate_distance_from_two_frames(8, 9, results))



print("Second comparison from a to b (should be different):")
print(calculate_distance_from_two_frames(0, 2, results))

print("Second comparison from a to c (should be different):")
print(calculate_distance_from_two_frames(0, 4, results))

print("Second comparison from a to d (should be different):")
print(calculate_distance_from_two_frames(0, 6, results))

print("Second comparison from a to e (should be different):")
print(calculate_distance_from_two_frames(0, 8, results))

##############


print("Second comparison from b to c (should be different):")
print(calculate_distance_from_two_frames(2, 4, results))

print("Second comparison from b to d (should be different):")
print(calculate_distance_from_two_frames(2, 6, results))

print("Second comparison from b to e (should be different):")
print(calculate_distance_from_two_frames(2, 8, results))

###################

print("Second comparison from c to d (should be different):")
print(calculate_distance_from_two_frames(4, 6, results))

print("Second comparison from c to e (should be different):")
print(calculate_distance_from_two_frames(4, 8, results))

###################

print("Second comparison from d to e (should be different):")
print(calculate_distance_from_two_frames(6, 8, results))





