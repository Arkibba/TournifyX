# Generated by Django 5.2 on 2025-05-02 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournifyx', '0004_alter_tournament_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='team_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
