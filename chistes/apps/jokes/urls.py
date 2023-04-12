from django.urls import include, path

from rest_framework import routers

from .views import JokeViewSet

router = routers.DefaultRouter()
router.register(r'', JokeViewSet, basename='joke')

urlpatterns = [
    path('', include(router.urls)),
]
