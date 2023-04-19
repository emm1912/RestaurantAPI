from rest_framework import serializers
from .models import Tables

class TablesSerializer(serializers.Serializer):
    tableNumber = serializers.CharField(max_length=4,source='table_number')
    seatingCapacity = serializers.IntegerField(source='seating_capacity')
    availabilityStatus = serializers.CharField(max_length=255,source='availability_status')

    def create(self, validated_data):
        return Tables.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.tableNumber = validated_data.get('tableNumber')
        instance.seatingCapacity = validated_data.get('seatingCapacity')
        instance.availabilityStatus = validated_data.get('availabilityStatus')
        instance.save()
        return instance
    
    
class TablesSerializerFullResponse(serializers.Serializer):
    id = serializers.IntegerField()
    tableNumber = serializers.CharField(max_length=4,source='table_number')
    seatingCapacity = serializers.IntegerField(source='seating_capacity')
    availabilityStatus = serializers.CharField(max_length=255,source='availability_status')
    createdAt = serializers.DateTimeField(source='created_timestamp')
    updatedAt = serializers.DateTimeField(source='updated_timestamp')

