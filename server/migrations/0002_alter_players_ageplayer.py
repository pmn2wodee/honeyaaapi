# Generated by Django 3.2 on 2021-04-27 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='players',
            name='agePlayer',
            field=models.IntegerField(),
        ),
    ]
