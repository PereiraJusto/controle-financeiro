from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Pessoa
from .serializers import PessoaSerializer

@api_view(['GET'])
def health_check(request):
    return Response({"status": "ok"})

class PessoaViewSet(ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
    http_method_names = ["get", "post"]
    