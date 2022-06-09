from django.db import models

# Create your models here.
class Estado(models.Model):
    name = models.CharField(max_length=45)

class Cidade (models.Model):
    Estado_id_estado = models.ForeignKey(
        Estado,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=45) 
