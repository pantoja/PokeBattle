# Generated by Django 2.2.11 on 2020-03-26 01:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('battles', '0010_battle_winner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='battle',
            options={'ordering': ['-pk']},
        ),
        migrations.AlterModelOptions(
            name='team',
            options={'ordering': ['-battle']},
        ),
    ]
