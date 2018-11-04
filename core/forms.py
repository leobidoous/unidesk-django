from django import forms

FAVORITE_COLORS_CHOICES = (
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
)

class CadastrarAlunoForm(forms.Form):
    university = forms.CharField(label='Universidade', max_length=100)
    departament = forms.CharField(label='Departamento', max_length=100)
    course = forms.CharField(label='Curso', max_length=100)
    name = forms.CharField(label='Nome', max_length=25)