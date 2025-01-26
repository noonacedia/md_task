from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from task_2.serializers import JsonFileInputSerializer
from task_2.service import GoodsCounter


class GetJsonFileCalculation(CreateAPIView):
    serializer_class = JsonFileInputSerializer
    service = GoodsCounter

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        counted_goods = self.service.count_goods(serializer.validated_data['json_file'])
        headers = self.get_success_headers(serializer.data)
        return Response(counted_goods, status=status.HTTP_201_CREATED, headers=headers)
