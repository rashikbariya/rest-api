from .models import Posts
from .serializers import PostSerializer
from rest_framework import generics

from django.contrib.auth.models import User
from rest_framework import permissions
from blog.permissions import IsOwnerOrReadOnly


class PostAPIList(generics.ListCreateAPIView):
    # queryset = Posts.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def get_queryset(self):
        qs = Posts.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    queryset = Posts.objects.all()
    serializer_class = PostSerializer




# class UserList(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer