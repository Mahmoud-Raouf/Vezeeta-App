from rest_framework import viewsets
from blog.models import Post , Comment
from .serializers import PostSerializer , CommentSerializer
import django_filters.rest_framework #To import filter 

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend] # To run filter with Profile API
    filter_fields = ( 'title' , 'short_description')
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend] # To run filter with Profile API
    filter_fields = ( 'create_at' , 'name' , 'email')