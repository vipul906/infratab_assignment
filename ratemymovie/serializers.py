from rest_framework import serializers
from ratemymovie.models import Movie, PeopleRating


class PeopleRatingSerializer(serializers.ModelSerializer):
    """
        class for people rating Serializer
    """

    class Meta:
        model = PeopleRating
        fields = ["id", "movie", 'name', 'rating', 'date_created', 'date_modified']
        read_only_fields = (['name'])

    def validate(self, data):
        user = None
        # fetching the user from the request
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
        # owner of the movie can't rate their movie, checking the requested user with selected movie owner
        if user == data['movie'].owner:
            raise serializers.ValidationError({'error': "owner of the movie cannot rate their movie"})
        return data


class MovieSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    owner = serializers.ReadOnlyField(source='owner.username')
    people = PeopleRatingSerializer(many=True, read_only=True)

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Movie
        fields = ('id', "people", 'movie_name', 'owner', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')
