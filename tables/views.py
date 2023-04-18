from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework import status
from .models import Tables
from .serializers import TablesSerializer, TablesSerializerFullResponse


@api_view(['POST'])
def tables_list(request):
    serializer = TablesSerializer(data=request.data)
    data=request.data
    table_number = data["tableNumber"]
    serializer.is_valid(raise_exception=True)
    serializer.save()
    table = Tables.objects.get(table_number=table_number)
    serializerFullResponse = TablesSerializerFullResponse(table)
    return Response(serializerFullResponse.data, status=status.HTTP_201_CREATED)

    #Si se quiere get y post
    # if request.method == 'GET':
    #     query_set = Tables.objects.all()
    #     serializer = TablesSerializer(query_set, many=True)
    #     return Response(serializer.data) 
    # elif request.method == 'POST':
    #     serializer = TablesSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def tables_item(request, id):
    tables = get_object_or_404(Tables, pk=id)
    if request.method == 'GET':
        serializer = TablesSerializer(tables)
        serializerFullResponse = TablesSerializerFullResponse(tables)
        return Response(serializerFullResponse.data)
    elif request.method == 'PUT':       ####AQUI REVISAR
        table_object = Tables.objects.get(pk=id)
        data = request.data

        table_object.table_number = data.get("tableNumber", table_object.table_number)  #Con el get de aqui revisa si tiene el valor "data" si no regresa el valor existente (valor viejo)
        table_object.seating_capacity = data["seatingCapacity"]
        table_object.availability_status = data["availabilityStatus"]
        table_object.save()
        table = Tables.objects.get(pk=id)
        serializerFullResponse = TablesSerializerFullResponse(table)
        return Response(serializerFullResponse.data)

        #DE https://www.youtube.com/watch?v=f2xky4CwQ9Q  (4:09MIN)   SI FUNCIONA 
        # table_object.table_number = data.get("tableNumber", table_object.table_number)
        # table_object.seating_capacity = data.get("seatingCapacity", table_object.seating_capacity)
        # table_object.availability_status = data.get("availabilityStatus", table_object.availability_status)
        # table_object.save()
        # serializer = TablesSerializer(table_object)
        # return Response(serializer.data)

        #DE MOSH NO ME FUNCIONO A MI EN ESTE EJEMPLO
        # serializer = TablesSerializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
        # table = Tables.objects.get(pk=id)
        # serializerFullResponse = TablesSerializerFullResponse(table)
        # return Response(serializer.data)
    elif request.method == 'DELETE':
        table = Tables.objects.get(pk=id)
        serializerFullResponse = TablesSerializerFullResponse(table)
        tables.delete()
        return Response(serializerFullResponse.data, status=status.HTTP_204_NO_CONTENT)

