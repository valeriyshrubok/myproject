from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from .serializers import EmployeeSerializer
from ..models import Employee

class EmployeeListAPIView(ListAPIView):

    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

    filter_backends = [SearchFilter]
    search_fields = ['lvl']

    permission_classes = [IsAuthenticated]





