from django.urls import path
from .views import B_BoardList

urlpatterns = [
    path('list/', B_BoardList.as_view()),
]
