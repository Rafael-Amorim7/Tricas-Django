from django.shortcuts import render
from happy.models import Doacao, User, Institution
import folium
import geocoder

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

def map(req, location):
    location = geocoder.osm(str(location))
    if (location.lat == None):
        location = geocoder.osm('São Paulo')
    lat = location.lat
    lng = location.lng
    country = location.country
    # Create Map Object
    m = folium.Map(location=[lat, lng], zoom_start=100)
    folium.Marker([lat,lng], tooltip='Clique para mais informações', popup=country).add_to(m)
    m = m._repr_html_()
    data={
        'm':m,
    }
    return render(req, 'map.html', data)
