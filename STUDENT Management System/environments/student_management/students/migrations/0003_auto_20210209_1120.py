# Generated by Django 3.1.6 on 2021-02-09 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_students'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(max_length=11),
        ),
    ]
