from catalog.utils import *
from catalog.models import *

class Controle():

    def salvar_aluno(self):

        lines = read_file()

        _nome = get_nome(lines)
        _cpf = get_cpf(lines)
        _sexo = get_sexo(lines)
        _matricula = get_matricula(lines)
        _dt_nascimento = get_dt_nascimento(lines)
        _disciplinas = get_disciplinas(lines)

        for i in range(len(lines)):
            self.aluno = AlunoModel()

            self.aluno.nome_aluno = _nome[i]
            self.aluno.dt_nascimento = _dt_nascimento[i]
            self.aluno.sexo = _sexo[i]
            self.aluno.cpf = _cpf[i]
            self.aluno.matricula = _matricula[i]

            try:
                self.aluno.save()
            except:
                pass

            for j in range(len(_disciplinas[i])):
                self.disciplinas = DisciplinaModel()
                self.disciplinas.nome_disciplina = _disciplinas[i][j]
                try:
                    self.disciplinas.save()
                except:
                    pass

        # print('sdfojsdfljlkj')
        # print(self.disciplinas.nome_disciplina)
        # self.aluno.id_disciplinas.add(self.disciplinas)
                try:
                    self.aluno.id_disciplinas.add(self.disciplinas)
                except:
                    pass
