from django.urls import path
from .views import add_tea, home, tea_table, tea_quiz, quiz_results

urlpatterns = [
    path('',  home, name='home_page'), 
    path('add-tea/', add_tea, name='add_tea'), 
    path('table/' , tea_table, name = "tea_table"),
    path('practice/', tea_quiz, name='tea_quiz'),
    path('practice/result/', quiz_results, name='quiz_results'),
]