# Generated by Django 2.2.10 on 2020-02-28 21:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('battles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('battle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='battle', to='battles.Battle')),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trainer', to=settings.AUTH_USER_MODEL, verbose_name='Trainer')),
            ],
        ),
    ]
