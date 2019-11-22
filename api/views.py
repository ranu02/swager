from api.models import Cities
from common.viewsets import CustomModelViewSet
from api.serializers import CitiesSerializer
from common.utils import custom_response, custom_error_response, is_int
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class CitiesViewSet(CustomModelViewSet):
    """
    Signup view-set is used for signup process.
    """
    permission_classes = (IsAuthenticated, )
    http_method_names = ('get', 'post', 'delete')
    queryset = Cities.objects.all().order_by('id')

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CitiesSerializer
        return CitiesSerializer

    def create(self, request, *args, **kwargs):
        serializer = CitiesSerializer(data=request.data, context={"user": self.request.user})
        if serializer.is_valid():
            serializer.save()
            return custom_response(status=status.HTTP_201_CREATED, data=None, detail="success")
        return custom_error_response(status=status.HTTP_400_BAD_REQUEST, detail=list(serializer.errors.values())[0][0])