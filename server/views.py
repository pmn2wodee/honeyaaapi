from rest_framework.response import Response
from server.serializers import PersonSerializer,GetUIDSerializer
from server.models import Person
from django.shortcuts import render
from rest_framework.views import APIView

class getinfo(APIView):
    def get (self,request, uid ):
        person = Person.objects.filter(uid = uid)
        serial = GetUIDSerializer(person, many = True)
        return Response(serial.data)

# Create your views here.
