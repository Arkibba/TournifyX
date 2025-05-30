# Generated by Django 5.2 on 2025-05-02 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournifyx', '0003_tournament_match_type_tournament_num_participants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='category',
            field=models.CharField(choices=[('valorant', 'Valorant'), ('football', 'Football'), ('cricket', 'Cricket'), ('chess', 'Chess')], max_length=20),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='match_type',
            field=models.CharField(choices=[('knockout', 'Knockout'), ('league', 'League')], default='knockout', max_length=10),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='num_participants',
            field=models.PositiveIntegerField(default=4),
        ),
    ]
