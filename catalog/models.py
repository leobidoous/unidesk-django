from django.db import models
from django.urls import reverse

# Create your models here.
class UniversidadeModel(models.Model):
    nome_universidade = models.CharField('Nome Universidade', max_length=100)
    create_at = models.DateTimeField('Criado em', auto_now_add=True)
    update_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Universidade'
        verbose_name_plural = 'Universidades'
        ordering = ['nome_universidade']

    def __str__(self):
        return self.nome_universidade

    def get_absolut_url(self):
        return reverse('list_view', kwargs={'universidade':self.nome_universidade})

class DepartamentoModel(models.Model):
    nome_departamento = models.CharField('Nome do Departamento', max_length=100)
    id_universidade = models.ForeignKey(UniversidadeModel, on_delete=models.CASCADE)
    create_at = models.DateTimeField('Criado em', auto_now_add=True)
    update_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
        ordering = ['nome_departamento']

    def __str__(self):
        return self.nome_departamento

class CursoModel(models.Model):
    nome_curso = models.CharField('Nome do Curso', max_length=100)
    id_departamento = models.ForeignKey(DepartamentoModel, on_delete=models.CASCADE)
    create_at = models.DateTimeField('Criado em', auto_now_add=True)
    update_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['nome_curso']

    def __str__(self):
        return self.nome_curso

class DisciplinaModel(models.Model):
    nome_disciplina = models.CharField('Nome da Disciplina', max_length=100)
    create_at = models.DateTimeField('Criado em', auto_now_add=True)
    update_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Disciplina'
        verbose_name_plural = 'Disciplinas'
        ordering = ['nome_disciplina']

    def __str__(self):
        return self.nome_disciplina

class AlunoModel(models.Model):
    nome_aluno= models.CharField('Nome do Aluno', max_length=25)
    id_universidade = models.ForeignKey(UniversidadeModel, on_delete=models.CASCADE)
    id_departamento = models.ForeignKey(DepartamentoModel, on_delete=models.CASCADE)
    id_curso = models.ForeignKey(CursoModel, on_delete=models.CASCADE)
    id_disciplinas = models.ManyToManyField(DisciplinaModel)
    create_at = models.DateTimeField('Criado em', auto_now_add=True)
    update_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
        ordering = ['nome_aluno']

    def __str__(self):
        return self.nome_aluno