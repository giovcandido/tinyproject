# Generated by Django 4.1.4 on 2022-12-06 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tinyapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tinymessage',
            options={'ordering': ['id']},
        ),
    ]