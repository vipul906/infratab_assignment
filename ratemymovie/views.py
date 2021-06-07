from rest_framework import viewsets, permissions
from django.http import HttpResponse
from rest_framework import serializers

from ratemymovie.serializers import MovieSerializer, PeopleRatingSerializer
from ratemymovie.models import Movie, PeopleRating
from ratemymovie.permissions import IsOwner


class MovieViewSet(viewsets.ModelViewSet):
    """
    View-set for movie list which can perform safe method of rest full api
    """
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def perform_update(self, serializer):
        movie_obj = serializer.validated_data

        movie_name = movie_obj.get('movie_name')
        queryset = Movie.objects.all()
        for item in queryset:
            if movie_name == item.movie_name:
                raise serializers.ValidationError(
                    {"error": f"{movie_name} is already exist and created by {item.owner}"})
        serializer.save()

    def perform_create(self, serializer):
        """Save the post data when creating a new Movie."""
        user = self.request.user
        movie_obj = serializer.validated_data
        movie_name = movie_obj.get('movie_name')
        queryset = Movie.objects.all()
        for item in queryset:
            if movie_name == item.movie_name:
                raise serializers.ValidationError(
                    {"error": f"{movie_name} is already exist and created by {item.owner}"})

        serializer.save(owner=user)


class PeopleRatingMovieViewSet(viewsets.ModelViewSet):
    """
    View-set for People list which can perform safe method of rest full api
    """
    queryset = PeopleRating.objects.all()
    serializer_class = PeopleRatingSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def perform_update(self, serializer):
        user = self.request.user
        people_rating_obj = serializer.validated_data
        movie_name = people_rating_obj.get('movie').movie_name
        rating = people_rating_obj.get('rating')
        queryset = PeopleRating.objects.all()
        for item in queryset:
            # checking if the user is rated this movie before
            if user.username == item.name and movie_name == item.movie.movie_name:
                if rating == item.rating:
                    raise serializers.ValidationError({"error": f"please change the rating while sending the request"})
                raise serializers.ValidationError({"error": f"you already rate this movie {movie_name}"})
        serializer.save()

    def perform_create(self, serializer):
        """Save the post data when rating a new Movie."""
        user = self.request.user
        people_rating_obj = serializer.validated_data
        movie_name = people_rating_obj.get('movie').movie_name
        queryset = PeopleRating.objects.all()
        for item in queryset:
            # checking if the user is rated this movie before
            if user.username == item.name and movie_name == item.movie.movie_name:
                raise serializers.ValidationError({"error": f"you already rate this movie {movie_name}"})
        serializer.save(name=user)


def index(request) -> HttpResponse:
    """
    Args:
        request:

    Returns:HttpResponse for list of movie

    """
    movie_list = Movie.objects.order_by('-id')[:]
    output = ''.join(['<a href="/movies_list/%s"><li>%s</li></>' % (q.id, q.movie_name) for q in movie_list])
    return HttpResponse(output)
