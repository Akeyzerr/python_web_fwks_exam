# Generated by Django 3.1.3 on 2020-12-05 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20201205_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='clean_quote_of_the_day',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False),
        ),
    ]
