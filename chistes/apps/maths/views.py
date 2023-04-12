import math

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.views import APIView


number_doc = openapi.Parameter(
    'number', openapi.IN_QUERY,
    description="A number to be incemented by one",
    type=openapi.TYPE_INTEGER
)
numbers_doc = openapi.Parameter(
    'numbers', openapi.IN_QUERY,
    description="A numbers to calculate least common multiplier",
    type=openapi.TYPE_ARRAY,
    items=openapi.Items(type=openapi.TYPE_INTEGER)
)


class MathAPI(APIView):

    @swagger_auto_schema(
        responses={
            200: '{"result": 56}',
        },
        manual_parameters=[number_doc, numbers_doc],
    )
    def get(self, request, format=None):
        numbers = request.query_params.get('numbers')
        number = request.query_params.get('number')

        if all([number, numbers]):
            raise APIException(
                'You must send the param number or numbers not both'
            )

        if not any([number, numbers]):
            raise APIException('You must send the param number or numbers')

        if numbers:
            numbers = numbers.split(',')
            data = {'result': math.lcm(*[int(element) for element in numbers])}

        if number:
            data = {'result': int(number) + 1}

        return Response(data)
