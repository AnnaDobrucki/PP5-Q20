from django.urls import path
from . import views

urlpatterns = [
    path('replies/', views.ReplyListView.as_view(), name='reply-list'),
    path('replies/<int:pk>/', views.ReplyDetailView.as_view(), name='reply-detail'),
]