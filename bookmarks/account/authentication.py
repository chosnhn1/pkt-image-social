from django.contrib.auth.models import User
from account.models import Profile

# make custom auth backend
# this can be done by construct two methods: authenticate() and get_user()
class EmailAuthBackend():
    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password): # type: ignore
                return user
            return None
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
        
def create_profile(backend, user, *args, **kwargs):
    """
    Create user profile for social authentication.
    """
    Profile.objects.get_or_create(user=user)