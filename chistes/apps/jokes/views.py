from random import choice

from rest_framework import mixins, serializers, viewsets
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Joke
from .services import joke_chuck, joke_dad

RANDOM_SRC = [joke_dad, joke_chuck]


class JokeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Joke
        fields = '__all__'


class JokeViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = JokeSerializer
    queryset = Joke.objects.all()


class RandomAPIView(APIView):
    def get(self, request, format=None):
        return Response({'text': choice(RANDOM_SRC)()})


class JokeBySourceAPIView(APIView):
     def get(self, request, slug, format=None):

        match slug:
            case 'Chuck':
                joke_text = joke_chuck()

            case 'Dad':
                joke_text = joke_dad()

            case _:
                raise APIException('Unexpected Joke Source')

        return Response({'text': joke_text})
