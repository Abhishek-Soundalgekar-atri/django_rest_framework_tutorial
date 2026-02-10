from rest_framework import viewsets, permissions
from django.contrib.auth.models import User
from .models import Snippet
from .serializers import SnippetSerializer, UserSerializer


class SnippetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows snippets to be viewed or edited.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer