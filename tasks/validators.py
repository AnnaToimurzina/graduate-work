from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from tasks import models
from tasks.models import Task
from tasks.serializers import BusyEmployeeSerializer


'''class BusyEmployeesAPIView(APIView):
    def get(self, request, format=None):
        # Получаем список занятых сотрудников, отсортированных по количеству активных задач
        queryset = Task.objects.filter(status__in=['pending', 'processing']).values('executor__id', 'executor__first_name', 'executor__last_name').annotate(active_tasks_count=models.Count('id')).order_by('-active_tasks_count')
        serializer = BusyEmployeeSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)'''