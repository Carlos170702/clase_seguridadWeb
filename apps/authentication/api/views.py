from rest_framework import generics, status
from rest_framework.response import Response
from apps.users.api.serializer import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from apps.utils.response import success_response, error_response


class Login(generics.CreateAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()

    def create(self, request, *args, **kwargs):
        body = request.data

        if 'username' not in body or 'password' not in body:
            return error_response('Credenciales no proporcionadas', status=status.HTTP_400_BAD_REQUEST)

        user = self.get_queryset().filter(username=body['username']).first()
        if user is None:
            return error_response('Credenciales no validas', status=status.HTTP_404_NOT_FOUND)

        if not user.password == body['password']:
            return error_response('Credenciales no validas', status=status.HTTP_400_BAD_REQUEST)

        if not user.is_active:
            return error_response('Usuario inactivo', status=status.HTTP_400_BAD_REQUEST)

        refresh = RefreshToken.for_user(user)
        access = refresh.access_token
        user = UserSerializer(user).data

        return success_response(data={
            'token': str(access),
            'refresh token': str(refresh),
            'user': user
        })
