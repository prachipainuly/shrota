from dtaidistance import dtw
import numpy as np

def compare_two_sequences(s1, s2):
    return dtw.distance(s1, s2)

