# Generated by Django 4.0.4 on 2022-06-09 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('happy', '0002_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50)),
                ('celular', models.CharField(max_length=11)),
                ('atividade', models.CharField(max_length=45)),
                ('descricao', models.TextField()),
                ('cep', models.CharField(max_length=9)),
                ('bairro', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=100)),
                ('situacao', models.CharField(max_length=1)),
                ('created_at', models.TimeField(auto_now=True)),
                ('updated_at', models.TimeField(auto_now=True)),
                ('Cidade_id_cidade', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='happy.cidade')),
                ('Estado_id_estado', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='happy.estado')),
            ],
        ),
    ]
