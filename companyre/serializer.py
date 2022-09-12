from rest_framework import serializers
from companyre.models import CompanyRecord

class ComapanySerializer(serializers.ModelSerializer):
    class Meta:
        model=CompanyRecord
        fields='__all__'