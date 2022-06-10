from django.db import models
from django.db.models.fields import IntegerField

# Create your models here.
class Estado(models.Model):
    name = models.CharField(max_length=45)

class Cidade (models.Model):
    Estado_id_estado = models.ForeignKey(
        Estado,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=45) 

class User(models.Model):
    Estado_id_estado = models.ForeignKey(
        Estado,
        on_delete=models.CASCADE,
        null=True
    )
    Cidade_id_cidade = models.ForeignKey(
        Cidade,
        on_delete=models.CASCADE,
        null=True
    )
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    celular = models.CharField(max_length=11)
    situacao = models.CharField(max_length=1)
    created_at = models.TimeField(auto_now=True)
    updated_at = models.TimeField(auto_now=True)

class Institution(models.Model):
    Estado_id_estado = models.ForeignKey(
        Estado,
        on_delete=models.CASCADE,
        null=True
    )
    Cidade_id_cidade = models.ForeignKey(
        Cidade,
        on_delete=models.CASCADE,
        null=True
    )
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    celular = models.CharField(max_length=11)
    atividade = models.CharField(max_length=45)
    descricao = models.TextField()
    cep = models.CharField(max_length=9)
    bairro = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    situacao = models.CharField(max_length=1)
    created_at = models.TimeField(auto_now=True)
    updated_at = models.TimeField(auto_now=True)

    @property
    def city(self):
        return Cidade.objects.get(pk=self.Cidade_id_cidade_id)
        
    @property
    def state(self):
        return Estado.objects.get(pk=self.Estado_id_estado_id)



class Doacao(models.Model):
    Instituicoes = models.ForeignKey(
        Institution,
        on_delete=models.CASCADE
    )
    User = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    ) 
    valor = IntegerField()
    horario = models.TimeField(auto_now=True)

    @property
    def user(self):
        return User.objects.get(pk=self.User_id)
        
    @property
    def instituicao(self):
        return Institution.objects.get(pk=self.Instituicoes_id)
