# Generated by Django 3.2.8 on 2021-10-24 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customUser', '0007_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.EmailField(max_length=150, null=True, unique=True, verbose_name='email address'),
        ),
    ]
