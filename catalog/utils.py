def read_file():
    with open('/home/leobidoous/Documentos/DJANGO/CADASTRO/core/static/data/alunos.txt', 'r') as file:
        lines = []
        for line in file:
            lines.append(line)
        return lines

def get_matricula(lines):
    matricula = []
    for _ in lines:
        matricula.append(_[:4])
    return matricula

def get_nome(lines):
    nomes = []
    for _ in lines:
        nome = _[4:29]
        aux1 = ''
        for i in range(len(nome)):
            if i == 0:
                aux1 = str(nome[i]).upper()
                aux1 += str(nome[i+1:]).lower()
            elif nome[i] == ' ' and nome[i-1] != ' ':
                aux2 = aux1[:i+1]
                aux1 = aux2
                aux1 += str(nome[i+1]).upper()
                aux1 += str(nome[i+2:]).lower()
        nomes.append(aux1)
    return nomes

def get_cpf(lines):
    cpf = []
    for _ in lines:
        cpf.append(_[29:40])
    return cpf

def get_sexo(lines):
    sexo = []
    for _ in lines:
        if _[40] == '1':
            sexo.append('Masculino')
        elif _[40] == '2':
            sexo.append('Feminino')
        else:
            sexo.append('Invalid')
    return sexo

def get_dt_nascimento(lines):
    dt_nascimento = []
    for _ in lines:
        data = str(_[41:43]) + '/'
        data += str(_[43:45]) + '/'
        data += str(_[45:49])
        dt_nascimento.append(data)
    return dt_nascimento

def get_disciplinas(lines):
    disciplinas = []
    for _ in lines:
        aux = []
        for i in range(0, len(_[49:-1]), 7):
            aux.append(_[49+i:49+i+7])
        disciplinas.append(aux)
    return disciplinas
