# Generated by Django 5.0.6 on 2024-07-14 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth2', '0006_code_alter_problemdetail_difficulty'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Code',
        ),
    ]