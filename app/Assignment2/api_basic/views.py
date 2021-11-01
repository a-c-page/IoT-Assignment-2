from rest_framework.parsers import JSONParser
from .models import State
from .serializers import StateSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def state(request):
    if request.method == 'GET':
        state = State.objects.all()
        serializer = StateSerializer(state, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = StateSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)