from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    def list(self, request):
        level = request.GET.get('level')
        if level:
            queryset = Employee.objects.filter(level=int(level))
        else:
            queryset = Employee.objects.all()
        serializer = EmployeeSerializer(queryset, many=True)
        return Response(serializer.data)
    def retrieve(self, request, pk=None):
        queryset = Employee.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = EmployeeSerializer(user)
        return Response(serializer.data)

    def get(self, request, format=None):
        content = {
            'status': 'request was permitted'
        }
        return Response(content)
