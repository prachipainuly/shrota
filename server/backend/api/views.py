import json
import random
import math
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import WordSerializer, UserSerializer, SignsSerializer
from shrota.models import Word, User, Signs


@api_view(['GET'])
def get_categories(request):
    category = {'count': 4, 'names': ["Fruits", "Greetings", "ASL Basics", "Alphabets"]}
    return Response(category)


@api_view(['GET'])
def get_all_words(request):
    words = Word.objects.all()
    serializer = WordSerializer(words, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_random_word(request):
    total_items = int(Word.objects.count())
    random_id = random.randint(0, total_items)
    word = Word.objects.get(id=random_id)
    serializer = WordSerializer(word, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def get_random_alphabets(request):
    random_id = random.sample(range(55, 80), 10)
    alphas = [Word.objects.get(id=x) for x in random_id]
    serializer = WordSerializer(alphas, many=True)
    return Response(serializer.data)


def calculate_distance_from_two_frames(user_vector, vocabulary):
    """
    Function to calculate difference between two hand vectors.
    :param user_vector:
    :param vocabulary:
    :return:
    """
    # At first we normalize the vector to landmark of writs (x/y/z_zero)
    x_zero = user_vector[0][0]
    y_zero = user_vector[1][0]
    z_zero = user_vector[2][0]

    # We also get the handsize to normalize points to hand_size
    handsize_reference = math.sqrt(
        (x_zero - user_vector[0][5]) ** 2 + (y_zero - user_vector[1][5]) ** 2 + (z_zero - user_vector[2][5]) ** 2)

    # Now based on the handsize_reference we can normalize landmarks to hand size

    for j in range(20):
        user_vector[0][j + 1] = (user_vector[0][j + 1] - x_zero) / handsize_reference
        user_vector[1][j + 1] = (user_vector[1][j + 1] - y_zero) / handsize_reference
        user_vector[2][j + 1] = (user_vector[2][j + 1] - z_zero) / handsize_reference

    # Now we get the hand mark vectors from our database:
    # res = getVectoryFromDatabase(vocabulary)
    res = Signs.objects.get(gesture=vocabulary)
    serializer = SignsSerializer(res, many=False)
    data = serializer.data
    vector = {'x': [], 'y': [], 'z': []}
    for i in vector.keys():
        for j in range(0, 21):
            vector[i].append(data[f'{i}{j}'])

    vector_from_database_x = vector['x']
    vector_from_database_y = vector['y']
    vector_from_database_z = vector['z']

    print(len(vector_from_database_x))
    print(len(vector_from_database_y))
    print(len(vector_from_database_z))

    x_zero = vector_from_database_x[0]
    y_zero = vector_from_database_y[0]
    z_zero = vector_from_database_z[0]

    # We do the same as above with  vectors from database:
    handsize_reference_database = math.sqrt(
        (vector_from_database_x[0] - vector_from_database_x[5]) ** 2 + (
                vector_from_database_y[0] - vector_from_database_y[5]) ** 2 +
        (vector_from_database_z[0] - vector_from_database_z[5]) ** 2)
    # Now based on the handsize_reference we can normalize landmarks to hand size
    for j in range(20):
        vector_from_database_x[j + 1] = (vector_from_database_x[j + 1] - x_zero) / handsize_reference_database
        vector_from_database_y[j + 1] = (vector_from_database_y[j + 1] - y_zero) / handsize_reference_database
        vector_from_database_z[j + 1] = (vector_from_database_z[j + 1] - z_zero) / handsize_reference_database

    # Now we calculate for each hand point the difference
    diff1 = 0
    for i in range(20):
        # for each landmark_point we compare difference:
        diff1 = diff1 + math.sqrt((user_vector[0][i + 1] - vector_from_database_x[i + 1]) ** 2 +
                                  (user_vector[1][i + 1] - vector_from_database_y[i + 1]) ** 2 +
                                  (user_vector[2][i + 1] - vector_from_database_z[i + 1]) ** 2)

    # Now we can finally return the difference!
    return diff1


@api_view(['POST'])
def calculate_round_result(request):
    try:
        body = dict(json.loads(request.body))
        vector = dict(body['right_handpoints']).values()
        alpha = str.upper(body['word'])
        difference = calculate_distance_from_two_frames(list(vector), alpha)
        if 0 <= difference <= 2:
            score = 50
        elif 1 <= difference <= 2.6:
            score = 40
        elif 2 <= difference <= 3.2:
            score = 30
        elif 3 <= difference <= 3.8:
            score = 20
        elif 4 <= difference <= 5:
            score = 10
        else:
            score = 0
        if score != 0:
            res = {'result': 'MATCHED', 'score': score}
        else:
            res = {'result': f'NOT MATCHED', 'score': score}
        return Response(res)
    except Exception as e:
        return Response({'result': f'error: {e}', 'score': None}, status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def add_random_word(request):
    serializer = WordSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def add_user_score(request):
    user = User.objects.get(name=request.data['name'])
    if not user:
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
    else:
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def get_leaderboard(request):
    user_data = User.objects.order_by('-score')
    serializer = UserSerializer(user_data, many=True)
    return Response(serializer.data)
