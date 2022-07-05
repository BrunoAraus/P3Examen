from urllib import response
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Suscripciones
from .serializers import SuscripcionesSerializer
@csrf_exempt
@api_view(['GET','POST'])
def lista_sus(request):
    if request.method == 'GET':
        sus = Suscripciones.objects.all()
        serializer = SuscripcionesSerializer(sus, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SuscripcionesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def detalle_sus(request,id):
    try:
        sus = Suscripciones.objects.get(codigo=id)
    except Suscripciones.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = SuscripcionesSerializer(sus)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SuscripcionesSerializer(sus, data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        sus.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


