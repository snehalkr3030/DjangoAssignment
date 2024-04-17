from rest_framework import serializers
from .models import Invoice

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['id', 'date', 'customer_name']

    def create(self, validated_data):
        return Invoice.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.date = validated_data.get('date', instance.date)
        instance.customer_name = validated_data.get('customer_name', instance.customer_name)
        instance.save()
        return instance
