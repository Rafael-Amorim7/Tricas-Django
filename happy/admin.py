from django.contrib import admin
from .models import Doacao, User, Institution

# Register your models here.
admin.site.register(User)
admin.site.register(Institution)
admin.site.register(Doacao)
