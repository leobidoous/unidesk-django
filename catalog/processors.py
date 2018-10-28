from catalog.models import UniversidadeModel


def Universidades(request):
    return {
                'Universidades': UniversidadeModel.objects.all()
            }