from django.db.models import Count
from rest_framework import viewsets

from .models import Cancion, Playlist
from .serializers import CancionSerializer, PlaylistSerializer

class CancionViewSet(viewsets.ModelViewSet):
    queryset = Cancion.objects.all()
    serializer_class = CancionSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        genero = self.request.query_params.get("genero")
        artista = self.request.query_params.get("artista")
        titulo = self.request.query_params.get("titulo")

        # filtros para la api :)
        if genero:
            queryset = queryset.filter(playlist__genero__icontains=genero)
        if artista:
            queryset = queryset.filter(artista__icontains=artista)
        if titulo:
            queryset = queryset.filter(titulo__icontains=titulo)

        return queryset.distinct()

class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = (
        Playlist.objects.annotate(num_canciones=Count("canciones"))
        .order_by('nombre')
    )
    serializer_class = PlaylistSerializer