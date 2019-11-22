"""
Authentication app serializer used for registration & login etc. purpose.
"""
from rest_framework import serializers
from api.models import Cities


class CitiesSerializer(serializers.ModelSerializer):
    """
    PolicyAndTermsUrl serializer.
    """
    class Meta:
        """
        PolicyAndTermsUrl meta class.
        """
        model = Cities
        fields = ('city_name', 'zipcode')
