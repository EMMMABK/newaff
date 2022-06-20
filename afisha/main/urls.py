from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Home'),
    path('movies', views.movies, name='Movies'),
    path('directors', views.directors, name='Directors'),
    path('reviews', views.reviews, name='Reviews'),
    path('movies/<int:id>/', views.Movie_Detail_View),
    path('directors/<int:id>', views.Director_Detail_View),
    path('reviews/<int:id>', views.Reviews_Detail_View)
]