# Generated by Django 3.1.2 on 2020-10-20 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viedo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viedo',
            name='vedioNumber',
            field=models.IntegerField(),
        ),
    ]