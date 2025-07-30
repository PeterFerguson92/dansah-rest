from rest_framework import generics, status
from rest_framework.response import Response

from .models import PowerLiving, MonthlyPowerLiving
from .powerlivingserializers import PowerLivingSerializer, MonthlyPowerLivingSerializer


class PowerLivingView(generics.GenericAPIView):
    serializer_class = PowerLivingSerializer
    queryset = PowerLiving.objects.all()

    def get(self, request):
        power_living = PowerLiving.objects.all()
        if not power_living:
            return Response(
                {"status": "No power living available"},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = self.serializer_class(power_living, many=True)
        return Response({"status": "success", "result": serializer.data})


class PowerLivingDetailView(generics.GenericAPIView):
    serializer_class = PowerLivingSerializer
    queryset = PowerLiving.objects.all()

    def get_power_living(self, pk):
        try:
            return PowerLiving.objects.get(pk=pk)
        except:
            return None

    def get(self, pk):
        power_living = self.get_power_living(pk=pk)
        if power_living is None:
            return Response(
                {"status": "fail", "message": f"Power living with Id: {pk} not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = self.serializer_class(power_living)
        return Response({"status": "success", "result": serializer.data})


class MonthlyPowerLivingView(generics.GenericAPIView):
    serializer_class = MonthlyPowerLivingSerializer
    queryset = MonthlyPowerLiving.objects.all()

    def get(self, request):
        monthly_power_living = MonthlyPowerLiving.objects.all()
        if not monthly_power_living:
            return Response(
                {"status": "No monthly power living available"},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = self.serializer_class(monthly_power_living, many=True)
        return Response({"status": "success", "monthly_power_living": serializer.data})


class MonthlyPowerLivingDetailView(generics.GenericAPIView):
    serializer_class = MonthlyPowerLivingSerializer
    queryset = MonthlyPowerLiving.objects.all()

    def get_detail(self, pk):
        print("11111")
        try:
            return MonthlyPowerLiving.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk):
        print("22222222222")
        powerLiving = self.get_detail(pk=pk)
        if powerLiving is None:
            return Response(
                {
                    "status": "fail",
                    "message": f"Monthly power living with Id: {pk} not found",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = self.serializer_class(powerLiving)
        return Response({"status": "success", "result": serializer.data})
