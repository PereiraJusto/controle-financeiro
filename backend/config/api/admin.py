from django.contrib import admin
from .models import Pessoa, Categoria, Lancamento


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

@admin.register(Lancamento)
class LancamentoAdmin(admin.ModelAdmin):
    list_display =("data_evento", "valor", "pessoa", "categoria", "ativo")