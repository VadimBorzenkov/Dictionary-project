# Generated by Django 4.2.6 on 2023-10-12 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('editing', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dictionary',
            old_name='eng_words',
            new_name='english',
        ),
        migrations.RenameField(
            model_name='dictionary',
            old_name='ru_words',
            new_name='russian',
        ),
    ]
