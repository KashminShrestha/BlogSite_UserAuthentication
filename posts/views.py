from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Post
from .serializers import PostSerializer
from posts.permissions import IsAuthorOrReadOnly

# from rest_framework import permissions


# Create your views here.


# class PostList(ListCreateAPIView):
#     permission_classes = (permissions.IsAuthenticated,)
#     queryset = Post.objects.all()  # Query the Post model
#     serializer_class = PostSerializer


# class PostDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


class PostList(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
