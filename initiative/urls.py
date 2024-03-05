from django.urls import path
from . import views

urlpatterns = [
    path('initiatives/', views.DNDInitiativeListView.as_view(), name='initiative-list'),
    path('initiatives/<int:pk>/', views.DNDInitiativeDetailedView.as_view(), name='initiative-detail'),
]
