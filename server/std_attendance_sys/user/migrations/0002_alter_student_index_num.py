# Generated by Django 5.0.6 on 2024-06-28 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='index_num',
            field=models.IntegerField(),
        ),
    ]
