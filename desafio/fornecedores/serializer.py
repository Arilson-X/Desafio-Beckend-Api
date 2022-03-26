from dataclasses import field
from rest_framework import serializers
from fornecedores.models import RegistroFornecedores

class RegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroFornecedores
        fields = '__all__'