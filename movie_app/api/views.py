from movie_app.models import Movie
from .serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view()
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many= True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_details(request, id):
    movie = Movie.objects.get(id= id)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)