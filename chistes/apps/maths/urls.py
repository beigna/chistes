from django.urls import path

from .views import MathAPI

app_name = 'maths'
urlpatterns = [
    path('', MathAPI.as_view()),
]
