from django.urls import path
from .views import DNDEventList, DNDEventDetail

urlpatterns = [
    path('dnd_events/', DNDEventList.as_view(), name='dnd-event-list'),
    path('dnd_events/<int:pk>/', DNDEventDetail.as_view(),
         name='dnd-event-detail'),
]
