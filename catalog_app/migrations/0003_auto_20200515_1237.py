# Generated by Django 3.0.6 on 2020-05-15 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_app', '0002_language'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['last_name']},
        ),
    ]