# Generated by Django 5.0.3 on 2024-05-12 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_newmeeting'),
    ]

    operations = [
        migrations.AddField(
            model_name='newmeeting',
            name='venue',
            field=models.CharField(default='DG Room', max_length=100),
        ),
    ]
