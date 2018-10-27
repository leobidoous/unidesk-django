from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'core/index.html')

def insert_view(request):
    return render(request, 'core/insert_view.html')

def list_view(request):
    return render(request, 'core/list_view.html')

def import_view(request):
    return render(request, 'core/import_view.html')

def report_view(request):
    return render(request, 'core/report_view.html')

def delete_view(request):
    return render(request, 'core/delete_view.html')

def update_view(request):
    return render(request, 'core/update_view.html')
