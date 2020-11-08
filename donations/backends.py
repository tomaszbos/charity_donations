from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user_model = get_user_model()
        if username is None:
            try:
                user = user_model.objects.get(email=kwargs['email'])
            except user_model.DoesNotExist:
                return None
            else:
                if user.check_password(password):
                    return user
            return None
        if username is not None:
            try:
                user = user_model.objects.get(username=username)
            except user_model.DoesNotExist:
                return None
            else:
                if user.check_password(password):
                    return user
            return None
