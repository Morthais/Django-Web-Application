"""Defines URL patterns for learning_logs."""
from django.urls import path, include
from . import views

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Show all topics
    path('topics/', views.topics, name='topics'),
    # Detail page for a single topic
    path('topics/(<topic_id>\d+)/', views.topic, name='topic'),
]
