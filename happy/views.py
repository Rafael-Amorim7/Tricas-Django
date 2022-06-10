from django.shortcuts import render
from django.db import models
from happy.models import Doacao, User, Institution

def home(req):
    return render(req, 'index.html')

def instituicoes(req):
    instituicoes = Institution.objects.all()
    dados = {
        'institutions' : instituicoes
    }
    return render(req, 'instituicoes.html', dados)

def usuarios(req):
    usuarios = User.objects.all()
    dados = {
        'users': usuarios
    }
    return render(req, 'usuarios.html', dados)

def doacao(req):
    doacao = Doacao.objects.all()
    data = {
        'doacoes': doacao,
    }
    return render(req, 'doacao.html', data)

def detail_institution(req, pk):
    institution = Institution.objects.get(pk = pk)
    data = {
        'institution': institution,
    }
    return render(req, 'detail_institution.html', data)