# Generated by Django 3.2.13 on 2022-11-20 03:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_skill'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['-created']},
        ),
    ]
