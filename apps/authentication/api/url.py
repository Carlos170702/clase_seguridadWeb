from rest_framework.urls import path
from apps.authentication.api.views import Login


urlpatterns = [
    path('Login/', Login.as_view(), name='login'),
]