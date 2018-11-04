from django.shortcuts import render
from catalog.models import *
from catalog.controller import *
from core.forms import *

# Create your views here.
def insert_view(request):
    content = {}
    content['form'] = CadastrarAlunoForm()
    return render(request, 'catalog/insert_view.html', content)

def list_view(request):

    Controle().salvar_aluno()

    content = {}
    content['Alunos'] = AlunoModel.objects.all()
    return render(request, 'catalog/list_view.html', content)

def import_view(request):
    return render(request, 'catalog/import_view.html')

def report_view(request):
    return render(request, 'catalog/report_view.html')

def delete_view(request):
    return render(request, 'catalog/delete_view.html')

def update_view(request):
    return render(request, 'catalog/update_view.html')