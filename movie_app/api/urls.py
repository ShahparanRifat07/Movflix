from django.urls import path
from .views import movie_list,movie_details

urlpatterns = [
    path('list/',movie_list),
    path('<int:id>',movie_details),
]