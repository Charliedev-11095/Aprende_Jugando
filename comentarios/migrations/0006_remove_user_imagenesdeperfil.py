# Generated by Django 4.0.5 on 2022-08-08 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0005_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='imagenesdeperfil',
        ),
    ]
