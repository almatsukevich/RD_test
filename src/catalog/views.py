from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeView(viewsets.ViewSet):
    def list(self, request):
        queryset = Employee.objects.all()
        serializer = EmployeeSerializer(queryset, many=True)
        return Response(serializer.data)
    def retrieve(self, request, pk=None):
        queryset = Employee.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = EmployeeSerializer(user)
        return Response(serializer.data)

