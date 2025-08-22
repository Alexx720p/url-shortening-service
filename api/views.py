import string, random
from .models import Url
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializer import UrlSerializer

def generate_code(length=6):
    characters = string.ascii_letters + string.digits
    while True:
        code = ''.join(random.choices(characters, k=length))
        if not Url.objects.filter(short_code=code).exists():
            return code

class UrlCreate(APIView):
    def post(self, request):
        serializer = UrlSerializer(data=request.data)
        if serializer.is_valid():
            short_code = generate_code()
            serializer.save(short_code=short_code)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UrlRetrieve(APIView):
    def get(self, request, short_code):
        url = get_object_or_404(Url, short_code=short_code)
        url.access_count +=1
        url.save(update_fields=['access_count'])
        return Response(UrlSerializer(url).data)

class UrlUpdate(APIView):
    def put(self, request, short_code):
        url = get_object_or_404(Url, short_code=short_code)
        serializer = UrlSerializer(url, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UrlDelete(APIView):
    def delete(self, request, short_code):
        url = get_object_or_404(Url, short_code=short_code)
        url.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UrlStats(APIView):
    def get(self, request, short_code):
        url = get_object_or_404(Url, short_code=short_code)
        return Response({
            'original_url': url.original_url,
            'short_code': url.short_code,
            'access_count': url.access_count,
            'created_at': url.created,
            'updated_at': url.updated
        })