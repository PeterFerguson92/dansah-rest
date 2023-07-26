from rest_framework import status, generics
from rest_framework.response import Response

from .models import Profile
from .profilesserializers import ProfileSerializer


class ProfilesView(generics.GenericAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def get(self, request):
        profiles = Profile.objects.all()
        print(profiles)
        if not profiles:
            return Response(
                {"status": "No profile infdfedfformation available"},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = self.serializer_class(profiles, many=True)
        return Response({"status": "success", "result": serializer.data})
