from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import Record
from api.serializers import RecordSerializer


# http://www.tomchristie.com/rest-framework-2-docs/api-guide/viewsets
class RecordViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows records to be viewed or edited.
    """

    queryset = Record.objects.all().order_by("-posted")
    serializer_class = RecordSerializer
