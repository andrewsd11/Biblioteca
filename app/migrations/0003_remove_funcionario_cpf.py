# Generated by Django 5.0.3 on 2024-03-12 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_funcionario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='funcionario',
            name='cpf',
        ),
    ]
