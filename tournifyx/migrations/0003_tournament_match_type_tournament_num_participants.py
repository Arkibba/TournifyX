# Generated by Django 5.2 on 2025-05-02 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournifyx', '0002_category_tournament_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='match_type',
            field=models.CharField(choices=[('Knockout', 'Knockout'), ('League', 'League')], default='Knockout', max_length=10),
        ),
        migrations.AddField(
            model_name='tournament',
            name='num_participants',
            field=models.PositiveIntegerField(default=2),
        ),
    ]
