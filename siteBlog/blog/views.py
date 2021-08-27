from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def blogOverview(request):
    api_urls = {
        'List Posts': 'posts'
    } 
    return Response(api_urls)