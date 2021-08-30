from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer
from django.db.models import F

from .models import Post

@api_view(['GET'])
def blogOverview(request):
    api_urls = {
        'List Posts': 'posts',
        'Create Posts' : 'create-post'
    } 
    return Response(api_urls)

@api_view(['GET'])
def listPosts(request):
    posts = Post.objects.all().select_related('autor')
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def listPost(request, slug):
    post = Post.objects.get(slug=slug)
    serializer = PostSerializer(post)
    return Response(serializer.data)

@api_view(['POST'])
def createPost(request):
    serializer = PostSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)