import math

from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.views import APIView


class MathAPI(APIView):

    def get(self, request, format=None):
        numbers = request.query_params.getlist('numbers')
        number = request.query_params.get('number')

        if all([number, numbers]):
            raise APIException(
                'You must send the param number or numbers not both'
            )

        if not any([number, numbers]):
            raise APIException('You must send the param number or numbers')

        if numbers:
            data = {'result': math.lcm(*[int(element) for element in numbers])}

        if number:
            data = {'result': int(number) + 1}

        return Response(data)
