from django.contrib.auth.models import User, Group
from rest_framework import serializers
from shrota.models import Word, User


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
