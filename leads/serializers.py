from rest_framework import serializers
from .models import Lead


class LeadSerializer(serializers.ModelSerializer):

    assigned_to = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Lead
        fields = '__all__'