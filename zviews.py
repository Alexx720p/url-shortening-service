from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404, redirect
from .api.models import Url
import string, random
from rest_framework.generics import CreateAPIView
from .api.serializer import UrlSerializer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.utils.crypto import get_random_string
import json
from django.http import JsonResponse

# from django.shortcuts import get_object_or_404, redirect
# from .models import Url
# import string, random


# def redirect_short_url(request, short_code):
#     url_obj = get_object_or_404(Url, short_code=short_code)
#     url_obj.access_count +=1
#     url_obj.save(update_fields=['access_count'])
#     return redirect(url_obj.original_url)




class RedirectShortUrlView(APIView):
    def redirect_short_url(self, request, short_code):
        url_obj = get_object_or_404(Url, short_code=short_code)
        url_obj.access_count +=1
        url_obj.save(update_fields=['access_count'])
        return redirect(url_obj.original_url)

def generate_unique_code(lenght=6):
    characters = string.ascii_letters + string.digits
    while True:
        short_code = ''.join(random.choices(characters, k=lenght))
        if not Url.objects.filter(short_code=short_code).exists():
            return short_code


# @method_decorator(csrf_exempt, name='dispatch')
# class UrlCreateView(CreateAPIView):
#     serializer_class = UrlSerializer
    
#     def perform_create(self, serializer):
#         short_code = generate_unique_code()
#         serializer.save(short_code=short_code)

#     def create(self, request, *args, **kwargs):
#         response = super().create(request, *args, **kwargs)
#         short_code = response.data.get('short_code')
#         short_url = f'https://yourdomain.com/{short_code}'
#         return Response({'short_url': short_url}, status=status.HTTP_201_CREATED)


# class UrlShorten(APIView):
#     def post(self, request):
#         serializer = UrlSerializer(data=request.data)
#         if serializer.is_valid():
#             short_code = get_random_string(length=6)
#             serializer.save(shortCode=short_code)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def shorten_url(request):
    if request.methot == 'POST':
        data = json.loads(request.body)
        original_url = data.get('url')
        return JsonResponse({'shortcode': 'abc123'})
    return JsonResponse({'error': 'Method not allowed'}, status=405)
