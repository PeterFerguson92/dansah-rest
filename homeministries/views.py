from rest_framework import status, generics
from rest_framework.response import Response

from .homeministriesserializers import (
    HomeMinistriesSerializer,
)
from .models import HomeMinistries


class HomeMinistriesView(generics.GenericAPIView):
    serializer_class = HomeMinistriesSerializer
    queryset = HomeMinistries.objects.all()

    def get(self, request):
        home_ministries_material = HomeMinistries.objects.all()
        if not home_ministries_material:
            return Response(
                {"status": "No home ministries available"},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = self.serializer_class(home_ministries_material, many=True)
        return Response({"status": "success", "result": serializer.data})
