from rest_framework import serializers

from ..models import Employee, Position, Chief, Salary, Salary_info

class PositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Position
        fields = '__all__'

class ChiefSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chief
        fields = '__all__'

class SalarySerializer(serializers.ModelSerializer):

    class Meta:
        model = Salary
        fields = '__all__'

class PaidSalarySerializer(serializers.ModelSerializer):

    class Meta:
        model = Salary_info
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):

    name = serializers.CharField(required=True)
    position_id = PositionSerializer()
    chief_id = ChiefSerializer()
    salary_id = SalarySerializer()
    paid_salary_id = PaidSalarySerializer()

    class Meta:
        model = Employee
        fields = '__all__'