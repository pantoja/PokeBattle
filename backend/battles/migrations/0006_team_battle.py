# Generated by Django 2.2.11 on 2020-03-05 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('battles', '0005_remove_team_battle'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='battle',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='battle', to='battles.Battle'),
            preserve_default=False,
        ),
    ]
