from django.db import models

# Create your models here.
class UniversidadeModel(models.Model):
    nome_universidade = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_universidade

    class Meta:
        def __str__(self):
            pass

class DepartamentoModel(models.Model):
    nome_departamento= models.CharField(max_length=100)
    id_universidade = models.ForeignKey(UniversidadeModel, on_delete=models.CASCADE)



class CursoModel(models.Model):
    nome_curso = models.CharField(max_length=100)
    id_departamento = models.ForeignKey(DepartamentoModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_curso

    class Meta:
        def __str__(self):
            pass

class DisciplinaModel(models.Model):
    nome_disciplina = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_disciplina

    class Meta:
        def __str__(self):
            pass

class AlunoModel(models.Model):
    nome_aluno= models.CharField(max_length=100)
    id_universidade = models.ForeignKey(UniversidadeModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_aluno

    class Meta:
        def __str__(self):
            pass