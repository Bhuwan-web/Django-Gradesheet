# Generated by Django 3.2.8 on 2021-10-24 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customUser', '0005_alter_user_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=150, null=True, unique=True),
        ),
    ]
