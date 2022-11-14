from rest_framework import serializers

from fortesting.models import DummyModel

class DummySeriallizer(serializers.ModelSerializer):
    
    class Meta:
        model = DummyModel
        fields = '__all__'