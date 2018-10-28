from django.contrib import admin
from catalog.models import *
# Register your models here.

class UniversidadeConfig(admin.ModelAdmin):
    list_display = ['nome_universidade', 'create_at', 'update_at']
    search_fields = ['nome_universidade']
    list_filter = ['create_at', 'update_at']


class DepartamentoConfig(admin.ModelAdmin):
    list_display = ['nome_departamento', 'create_at', 'update_at']
    search_fields = ['nome_departamento']
    list_filter = ['create_at', 'update_at']


class CursoConfig(admin.ModelAdmin):
    list_display = ['nome_curso', 'create_at', 'update_at']
    search_fields = ['nome_curso']
    list_filter = ['create_at', 'update_at']


class DisciplinaConfig(admin.ModelAdmin):
    list_display = ['nome_disciplina', 'create_at', 'update_at']
    search_fields = ['nome_disciplina']
    list_filter = ['create_at', 'update_at']


class AlunoConfig(admin.ModelAdmin):
    list_display = ['nome_aluno', 'id_universidade', 'id_departamento', 'id_curso', 'create_at', 'update_at']
    search_fields = ['nome_aluno'],
    list_filter = ['create_at', 'update_at']


admin.site.register(UniversidadeModel, UniversidadeConfig)
admin.site.register(DepartamentoModel, DepartamentoConfig)
admin.site.register(CursoModel, CursoConfig)
admin.site.register(DisciplinaModel, DisciplinaConfig)
admin.site.register(AlunoModel, AlunoConfig)