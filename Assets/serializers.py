# Rest Framework Imports
from rest_framework import serializers

# Own imports
from Assets.models import Company

class CompanyModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Company