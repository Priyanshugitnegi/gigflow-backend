from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import Lead
from .serializers import LeadSerializer


class LeadListCreateView(generics.ListCreateAPIView):

    serializer_class = LeadSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Lead.objects.all()

    def perform_create(self, serializer):
        serializer.save()


class LeadDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    permission_classes = [AllowAny]