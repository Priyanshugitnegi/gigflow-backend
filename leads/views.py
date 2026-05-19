from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Lead
from .serializers import LeadSerializer


class LeadListCreateView(generics.ListCreateAPIView):

    serializer_class = LeadSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Lead.objects.all()

    def perform_create(self, serializer):
        serializer.save(assigned_to=self.request.user)


class LeadDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    permission_classes = [IsAuthenticated]