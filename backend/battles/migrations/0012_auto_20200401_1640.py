# Generated by Django 2.2.11 on 2020-04-01 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0002_auto_20200304_2045'),
        ('battles', '0011_auto_20200326_0125'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='first_pokemon',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='first_pokemon', to='pokemon.Pokemon'),
        ),
        migrations.AddField(
            model_name='team',
            name='second_pokemon',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='second_pokemon', to='pokemon.Pokemon'),
        ),
        migrations.AddField(
            model_name='team',
            name='third_pokemon',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='third_pokemon', to='pokemon.Pokemon'),
        ),
    ]
