from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_player, name='register_player'),
    path('submit-score/', views.submit_score, name='submit_score'),
    path('leaderboard/', views.get_leaderboard, name='get_leaderboard'),
    # Removed 'history/' path
]