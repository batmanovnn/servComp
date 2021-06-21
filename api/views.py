from django.views.generic import TemplateView, ListView
from rest_framework import generics, permissions
from . import serializers
from django.contrib.auth.models import User
from .models import Post, Comment, Category, Issue
from .serializers import PostSerializer
from .permissions import IsOwnerOrReadOnly


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


# class PostList(generics.ListCreateAPIView):
#     template_name = "table.html"
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)

class PostList(ListView):
    template_name = "table.html"
    model = Issue
    queryset = Issue.objects.all()
    # serializer_class = PostSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        return context

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


class HomePageView(TemplateView):

    template_name = "index.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['latest_articles'] = Article.objects.all()[:5]
    #     return context

class AboutPageView(TemplateView):

    template_name = "about.html"