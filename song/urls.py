from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.ListSong.as_view()),
    path('<int:pk>/', views.DetailSong.as_view()),
]
