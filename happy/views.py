from django.shortcuts import render
from happy.models import User, Institution

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
    data = {
    }
    return render(req, 'doacao.html', data)

def cadastro_cliente(req):
    #users = {'users': UserForm()}
    return render(req, 'cadastro_cliente.html')

#def create_cliente(req):
    #form = UserForm(req.POST or None)
    #if form.is_valid():
    #    form.save()
    #    return redirect('home')

#def cadastro_instituicao(req):
#    institutions = {}
#    institutions['institutions'] = InstitutionForm()    
#    return render(req, 'cadastro.html', institutions)

#def create(req):
#    form = InstitutionForm(req.POST or None)
#    if form.is_valid():
#        form.save()
#        return redirect('home')

#def createDoacao(req):
#    print(req.POST)
#    form = DoacaoCompForm(req.POST or None)
#    if form.is_valid():
#        form.save()
#        enviarEmail(req.POST.get('User'))
#        return redirect('home')

#def edit(req, pk):
#    data = {}
#    data['db'] = Institution.objects.get(pk = pk)
#    data['institutions'] = InstitutionForm(instance=data['db'])
#    return render(req, 'cadastro.html', data)

#def update(req, pk):
#    data = {}
#    data['db'] = Institution.objects.get(pk = pk)
#    form = InstitutionForm(req.POST or None, instance=data['db'])
#    if form.is_valid():
#        form.save()
#        return redirect('home')

#def edit2(req, pk):
#    data = {}
#    data['db'] = User.objects.get(pk = pk)
#    data['users'] = UserForm(instance=data['db'])
#    return render(req, 'cadastro2.html', data)

#def update2(req, pk):
#    data = {}
#    data['db'] = User.objects.get(pk = pk)
#    form = UserForm(req.POST or None, instance=data['db'])
#    if form.is_valid():
#        form.save()
#        return redirect('home')

#def editDoacao(req, pk):
#    data = {}
#    data['db'] = Doacao.objects.get(pk = pk)
#    data['doacao'] = DoacaoForm(instance=data['db'])
#    data['institutions'] = Institution.objects.values('id', 'email')
#    data['users'] = User.objects.values('id', 'email')
#    return render(req, 'doacao.html', data)

#def updateDoacao(req, pk):
#    data = {}
#    data['db'] = Doacao.objects.get(pk = pk)
#    form = DoacaoCompForm(req.POST or None, instance=data['db'])
#    if form.is_valid():
#        form.save()
#        return redirect('home')

#def delete(req, pk):
#    db = Institution.objects.get(pk = pk)
#    db.delete()
#    return redirect('home')

#def delete2(req, pk):
#    db = User.objects.get(pk = pk)
#    db.delete()
#    return redirect('home')

#def deleteDoacao(req, pk):
#    db = Doacao.objects.get(pk = pk)
#    db.delete()
#    return redirect('home')
