from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer

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
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createPost(request):
    serializer = PostSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)