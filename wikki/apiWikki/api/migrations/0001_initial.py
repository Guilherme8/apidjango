# Generated by Django 3.0.3 on 2020-02-17 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('descricao', models.TextField()),
                ('preco', models.FloatField()),
                ('data_criacao', models.DateField()),
                ('estoque', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('senha', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=30)),
                ('primeiro_nome', models.CharField(max_length=20)),
                ('ultimo_nome', models.CharField(max_length=20)),
                ('endereco', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preco', models.FloatField()),
                ('data_criacao', models.DateField()),
                ('estoque', models.IntegerField()),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Produto')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Usuario')),
            ],
        ),
    ]