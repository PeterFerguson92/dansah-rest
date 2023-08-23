from rest_framework import status, generics
from rest_framework.response import Response

from .homeministriesserializers import HomeMinistriesSerializer, MinistriesSerializer
from .models import HomeMinistries, Ministries


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


class MinistryDetailView(generics.GenericAPIView):
    serializer_class = MinistriesSerializer

    def get_ministry(self, pk):
        try:
            return Ministries.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk):
        ministries = self.get_ministry(pk=pk)
        if ministries is None:
            return Response(
                {"status": "fail", "message": f"Ministry with Id: {pk} not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = self.serializer_class(ministries)
        return Response({"status": "success", "result": serializer.data})
