from django.urls import path
from .views import b_board

urlpatterns = [
    path('a/', b_board)
]
