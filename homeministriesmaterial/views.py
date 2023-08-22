from rest_framework import status, generics
from rest_framework.response import Response

from .homeministriesmaterialserializers import (
    HomeMinistriesMaterialSerializer,
)
from .models import HomeMinistriesMaterial


class HomeMinistriesMaterialView(generics.GenericAPIView):
    serializer_class = HomeMinistriesMaterialSerializer
    queryset = HomeMinistriesMaterial.objects.all()

    def get(self, request):
        home_ministries_material = HomeMinistriesMaterial.objects.all()
        if not home_ministries_material:
            return Response(
                {"status": "No home ministries materials available"},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = self.serializer_class(home_ministries_material, many=True)
        return Response({"status": "success", "result": serializer.data})
