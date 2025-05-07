from django.shortcuts import render

# Create your views here.
def index(request):
    return render(render, 'index.html')


def calcular(request):
    altura = float(request.GET.get('altura'))
    peso = float(request.GET.get('peso'))
    imc = peso / (altura*altura)

    if imc < 18.5:
        classificacao = 'Abaixo do peso'
    elif imc < 24.9:
        classificacao = 'Peso normal'
    elif imc < 29.9:
        classificacao = 'Sobrepeso'
    else:
        classificacao = 'Obesidade'

    contexto= {
        'imc': imc,
        'classificacao': classificacao,
        'altura': altura,
        'peso': peso,
    }
    return render(request, 'resultado_imc.html', contexto)
    