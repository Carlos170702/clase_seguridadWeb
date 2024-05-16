from rest_framework.authentication import get_authorization_header
from rest_framework_simplejwt.tokens import AccessToken


def createAccessToken(user):
    token = AccessToken.for_user(user)
    return token


def get_token(request):
    token = get_authorization_header(request)
    if token:
        try:
            token = token.split()[1].decode()
            return token
        except:
            return None
