# Generated by Django 4.0.5 on 2022-07-19 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EdbooksApp', '0003_autores'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='edad',
            field=models.IntegerField(null=True),
        ),
    ]
