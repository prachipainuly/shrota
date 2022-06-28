import random
from rest_framework.response import Response
from rest_framework.decorators import api_view
from shrota.models import Word, User
from .serializers import WordSerializer, UserSerializer


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


@api_view(['POST'])
def add_random_word(request):
    serializer = WordSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def add_user_score(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
