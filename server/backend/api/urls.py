from django.urls import path
from . import views

urlpatterns = [
    path('get_word/', views.get_random_word),
    path('get_all_words/', views.get_all_words),
    path('get_categories/', views.get_categories),
    path('add_word/', views.add_random_word),
    path('add_user/', views.add_user_score),
    path('get_random_alphabets/', views.get_random_alphabets),
    path('calculate_round_result/', views.calculate_round_result),
]
