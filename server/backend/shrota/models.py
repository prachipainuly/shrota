from django.db import models


class Word(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)


class User(models.Model):
    name = models.CharField(max_length=200)
    score = models.IntegerField(max_length=200)
