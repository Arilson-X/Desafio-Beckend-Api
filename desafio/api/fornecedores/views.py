from rest_framework import viewsets
from fornecedores.models import RegistroFornecedores
from fornecedores.serializer import RegistroSerializer

class RegistrosViewSet(viewsets.ModelViewSet):
    queryset = RegistroFornecedores.objects.all()
    serializer_class = RegistroSerializer
