from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from someapp.repository import SomeModelRepository
from someapp.serializers import SomeSerializer
from someapp.service import SomeModelService

# Can be initialized via DI container
some_model_service = SomeModelService(SomeModelRepository())


class SomeModelView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'somemodelview.html'

    def get(self, request):
        data = some_model_service.get_items()
        serializer = SomeSerializer(data, many=True)
        return Response({'routes': serializer.data}, status=status.HTTP_200_OK)
