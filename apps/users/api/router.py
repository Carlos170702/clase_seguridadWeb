from rest_framework.routers import DefaultRouter
from apps.users.api.views import UserView

router = DefaultRouter()

router.register('', UserView, basename='user')

urlpatterns = router.urls
