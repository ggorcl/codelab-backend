# Generated by Django 5.0.6 on 2024-07-13 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth2', '0004_problems_problemdetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problemdetail',
            name='difficulty',
            field=models.IntegerField(),
        ),
    ]
