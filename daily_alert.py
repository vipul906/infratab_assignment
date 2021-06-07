import os

import django


class DailyAlert:
    def __init__(self):
        self.user_dict = {}

    def fetch_rating_based_on_admin(self):
        movie_obj = Movie.objects.all()
        for item in movie_obj:
            owner = item.owner.username
            if not self.user_dict.get(owner):
                self.user_dict[owner] = []
            rating_object = PeopleRating.objects.filter(movie=item.id)
            rating_list = [res.rating for res in rating_object]
            if rating_list:
                average_rating = sum(rating_list) // len(rating_list)
            else:
                average_rating = None
            self.user_dict[owner].append([average_rating, item.movie_name])

    def send_alert(self):
        for user, movie_list in self.user_dict.items():
            print(user)
            print({'Average Rating of %s' % res[1]: res[0] for res in movie_list})


if __name__ == "__main__":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'infratab_test.settings')
    django.setup()
    from ratemymovie.models import Movie, PeopleRating

    obj = DailyAlert()
    obj.fetch_rating_based_on_admin()
    obj.send_alert()
