from django.shortcuts import render

# Incluir a classe httpresponse.
from django.http import HttpResponse

# Define uma function view chamada index.
def index(request):
#   return HttpResponse('Ola Django - index')
    return render(request, 'Index.html')# novo retorno

# Define uma function view chamada ola.
def ola(request):
    return HttpResponse


