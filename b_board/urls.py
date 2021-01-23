from django.urls import path
from .views import B_BoardList, B_BoardDetail, B_BoardCreate

urlpatterns = [
    path('list/', B_BoardList.as_view(), name='list'),
    path('detail/<int:pk>',B_BoardDetail.as_view(), name='detail'),
    path('create/', B_BoardCreate.as_view(), name='create'),
]
