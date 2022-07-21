from rest_framework import serializers
from shrota.models import Word, User, Signs


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        return User(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.score = validated_data.get('score', instance.score)
        instance.save()
        return instance


class SignsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signs
        fields = '__all__'
