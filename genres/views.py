from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from genres.models import Genres
from genres.serializers import GenreSerializer
from app.permissions import GlobalDefaultPermissions


class GenreCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions,)
    queryset = Genres.objects.all()
    serializer_class = GenreSerializer


class GenereRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions,)
    queryset = Genres.objects.all()
    serializer_class = GenreSerializer
