from donation.models import Donation
from rest_framework import generics, status
from rest_framework.response import Response

# Create your views here.

from .donationserializers import (
    DonationSerializer,
)


class DonationView(generics.GenericAPIView):
    serializer_class = DonationSerializer
    queryset = Donation.objects.all()

    def get(self, request):
        home_activities = Donation.objects.all()
        if not home_activities:
            return Response(
                {"status": "Donation information not available"},
                status=status.HTTP_204_NO_CONTENT,
            )
        serializer = self.serializer_class(home_activities, many=True)
        return Response({"status": "success", "result": serializer.data})
