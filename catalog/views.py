from django.shortcuts import render
from catalog.models import *

# Create your views here.
def insert_view(request):
    return render(request, 'catalog/insert_view.html')

def list_view(request, universidade):
    content = {}
    universidade = UniversidadeModel.objects.get(nome_universidade = universidade)
    content['Universidade'] = universidade
    content['Alunos'] = AlunoModel.objects.filter(id_universidade = universidade)
    return render(request, 'catalog/list_view.html', content)

def import_view(request):
    return render(request, 'catalog/import_view.html')

def report_view(request):
    return render(request, 'catalog/report_view.html')

def delete_view(request):
    return render(request, 'catalog/delete_view.html')

def update_view(request):
    return render(request, 'catalog/update_view.html')