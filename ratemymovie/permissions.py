from rest_framework.permissions import BasePermission, SAFE_METHODS
from ratemymovie.models import Movie, PeopleRating


class IsOwner(BasePermission):
    """Custom permission class to allow only owners to edit them."""

    def has_object_permission(self, request, view, obj):
        """Return True if permission is granted for safe method like GET,POST,OPTION."""
        if bool(request.method in SAFE_METHODS):
            return True
        # Return True if permission is granted for movie view set
        if isinstance(obj, Movie):
            return obj.owner.username == request.user.username
        # Return True if permission is granted for people rating view set
        if isinstance(obj, PeopleRating):
            return obj.name == request.user.username
