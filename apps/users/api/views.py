from rest_framework import viewsets, status
from apps.users.api.serializer import UserSerializer
from apps.utils.response import success_response, error_response


class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()

    def list(self, request, *args, **kwargs):
        users_serialized = self.get_serializer(
            self.get_queryset(), many=True).data
        return success_response(data=users_serialized)

    def create(self, request, *args, **kwargs):
        body = request.data
        serializer = self.get_serializer(data=body)

        if serializer.is_valid():
            serializer.save()
            return success_response(data=serializer.data)
        return error_response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
