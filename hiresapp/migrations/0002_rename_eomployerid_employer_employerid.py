# Generated by Django 4.0.5 on 2022-07-02 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hiresapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employer',
            old_name='eomployerId',
            new_name='employerId',
        ),
    ]