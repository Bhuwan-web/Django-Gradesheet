# Generated by Django 3.2.8 on 2021-10-19 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customUser', '0004_auto_20211019_0212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]
