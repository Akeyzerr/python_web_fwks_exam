# Generated by Django 3.1.3 on 2020-11-24 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_delete_upload'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Document',
        ),
        migrations.DeleteModel(
            name='PrivateDocument',
        ),
    ]