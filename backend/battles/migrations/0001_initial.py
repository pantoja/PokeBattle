# Generated by Django 2.2.10 on 2020-02-27 12:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Battle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_creator', to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
                ('user_opponent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_opponent', to=settings.AUTH_USER_MODEL, verbose_name='Opponent')),
            ],
        ),
    ]
