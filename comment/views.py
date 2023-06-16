from rest_framework import generics, permissions
from posts.permissions import IsAuthorOrAdminOrPostOwner
from .models import Comment
from . import serializers


class CommentCreateView(generics.CreateAPIView):
    serializer_class = serializers.CommentSerializers
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetailView(generics.RetrieveDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializers

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthorOrAdminOrPostOwner(),]
        return [permissions.AllowAny(),]