from rest_framework import serializers

from .models import *

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class DataItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataItem
        fields = '__all__'


        #name = serializers.CharField(max_length=255)
        #namefull = serializers.CharField(max_length=255)
        #rem = serializers.CharField(required=False, allow_blank=True)
        #uid = serializers.UUIDField()

class PostDataSerializer(serializers.Serializer):
    type = serializers.CharField(max_length=255)


class CustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'




class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class MatrixSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matrix
        fields = '__all__'

class ExpenditureSerializer(serializers.ModelSerializer):
    services = ServiceSerializer(many=True)
    matrix = MatrixSerializer(many=True)

    class Meta:
        model = Expenditure
        fields = '__all__'

    def create(self, validated_data):
        services_data = validated_data.pop('services')
        matrix_data = validated_data.pop('matrix')
        expenditure = Expenditure.objects.create(**validated_data)

        for service_data in services_data:
            service = Service.objects.create(**service_data)
            expenditure.services.add(service)

        for matrix_data in matrix_data:
            matrix = Matrix.objects.create(**matrix_data)
            expenditure.matrix.add(matrix)

        return expenditure
