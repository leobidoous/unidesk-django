# Generated by Django 2.1.2 on 2018-11-03 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disciplinamodel',
            name='nome_disciplina',
            field=models.CharField(max_length=100, verbose_name='Nome da Disciplina'),
        ),
    ]
