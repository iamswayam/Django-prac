from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import NoteSerializer
from .models import Note


def HomePage(request):
    return render(request, 'home.html')


class TestView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'Name': 'Swayam Siddha Panda',
            'Age': 26,
            'Role': 'Python Devloper'
        }
        return Response(data)

    def note(self, request, *args, **kwargs):
        serializer = NoteSerializer(data=request.data)

        serializer.is_valid()
        serializer.save()

        return Response(serializer.data)
