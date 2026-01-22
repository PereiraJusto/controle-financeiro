from django.contrib import admin
from .models import Pessoa, Categoria


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ("nome", "ativo", "criado_em", "atualizado_em")
    list_filter = ("ativo",)
    search_fields = ("nome",)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome", "ativo", "criado_em", "atualizado_em")
    list_filter = ("ativo",)
    search_fields = ("nome",)