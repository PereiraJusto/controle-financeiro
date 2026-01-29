from rest_framework import serializers

from .models import Pessoa

class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = [
            "id",
            "nome",
            "ativo",
            "criado_em",
            "atualizado_em"
        ]
        