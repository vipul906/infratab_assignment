from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from ratemymovie.models import Movie, PeopleRating


class ModelTestCase(TestCase):
    """This class defines the test suite for the Movie model."""

    def setUp(self):
        """Define the test client and other test variables."""
        movie_name = "Sultan"
        owner = User.objects.create(
            username='nobody'
        )
        self.movie_list = Movie(movie_name=movie_name, owner=owner)
        movie_list_deep = Movie.objects.create(movie_name='sultan', owner=owner)
        rating = 1
        self.people_rating = PeopleRating(name='nobody', movie=movie_list_deep, rating=rating)

    def test_model_can_create_a_movie(self):
        """Test the Movie model can create a Movie."""
        old_count = Movie.objects.count()
        self.movie_list.save()
        new_count = Movie.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_model_can_create_a_moviet(self):
        """Test the PeopleRating model can Rate a movie."""
        old_count = PeopleRating.objects.count()
        self.people_rating.save()
        new_count = PeopleRating.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        movie_name = "Sultan"
        owner = User.objects.create(
            username='jvipu'
        )
        self.movie_list = {"movie_name": movie_name, "owner": owner}
        self.client.force_authenticate(user=owner)
        self.response_1 = self.client.post(
            'http://localhost:8000/api/movies_list/',
            {"movie_name": "Sultan"},
            format="json")

    def test_api_can_create_a_movie(self):
        """Test the api has for movie creation capability."""
        self.assertEqual(self.response_1.status_code, status.HTTP_201_CREATED)

    def test_api_can_update_a_movie_with_owner(self):
        response = self.client.put(
            'http://localhost:8000/api/movies_list/1/',
            {"movie_name": "Aultan"},
            format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_update_a_movie_without_owner(self):
        owner = User.objects.create(
            username='nobody'
        )
        self.client.force_authenticate(user=owner)
        response = self.client.put(
            'http://localhost:8000/api/movies_list/1/',
            {"movie_name": "Aultan"},
            format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_api_can_create_rating(self):
        owner = User.objects.create(
            username='jmehu'
        )
        Movie.objects.create(owner=owner, movie_name='mehant')
        response_1 = self.client.post(
            'http://localhost:8000/api/rating/',
            {"raing": 5, "movie": 2},
            format="json")
        self.assertEqual(response_1.status_code, status.HTTP_201_CREATED)
