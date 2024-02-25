from django.urls import path
from .views import DNDEventList, DNDEventDetail

urlpatterns = [
    path('events/', DNDEventList.as_view(), name='dnd-event-list'),
    path('events/<int:pk>/', DNDEventDetail.as_view(), name='dnd-event-detail'),
]