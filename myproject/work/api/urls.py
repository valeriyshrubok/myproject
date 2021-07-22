from django.urls import path

from .api_views import EmployeeListAPIView

urlpatterns = [
    path('employee/', EmployeeListAPIView.as_view(), name='employee')
]