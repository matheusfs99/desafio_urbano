from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import PlanilhaForm

from ..processo.models import Processo


def cadastrar_processo(request):
    form = PlanilhaForm(request.POST or None, request.FILES or None)
    if request.POST:
        if form.is_valid():
            obj = form.save(commit=False)
            planilha = request.FILES['arquivo']
            with open(f'media/uploads/{planilha.name}', 'r') as p:
                for linha in p:
                    ln = linha.split(';')
                    ln[2] = ln[2].replace('\n', '')
                    if ln[0] != 'pasta':
                        Processo.objects.create(pasta=ln[0],
                                                comarca=ln[1],
                                                uf=ln[2])
            obj.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('/')
    return render(request, 'index.html', {'form': form})
