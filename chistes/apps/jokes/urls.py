from django.urls import include, path

from rest_framework import routers

from .views import JokeBySourceAPIView, JokeViewSet, RandomAPIView

router = routers.DefaultRouter()
router.register(r'', JokeViewSet, basename='joke')

urlpatterns = [
    path('random/', RandomAPIView.as_view()),
    path('random/<slug:slug>/', JokeBySourceAPIView.as_view()),
    path('', include(router.urls)),
]
