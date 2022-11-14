from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import DummySeriallizer
from fortesting.models import DummyModel


class DummyView(APIView):
    def get(self, request, *args, **kwargs):

        qs = DummyModel.objects.all()
        serializer = DummySeriallizer(qs, many=True, context={"request": request})
        return Response(serializer.data)
