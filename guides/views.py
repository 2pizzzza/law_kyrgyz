from rest_framework import generics

from .models import Guide
from .serializers import GuideSerializer


class GuideListCreateView(generics.ListCreateAPIView):
    queryset = Guide.objects.all()
    serializer_class = GuideSerializer


class GuideRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Guide.objects.all()
    serializer_class = GuideSerializer
