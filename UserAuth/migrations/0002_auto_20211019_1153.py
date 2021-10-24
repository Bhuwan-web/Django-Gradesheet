# Generated by Django 3.2.8 on 2021-10-19 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserAuth', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
        migrations.RemoveField(
            model_name='login',
            name='last_login',
        ),
        migrations.AddField(
            model_name='login',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='Email Address'),
        ),
    ]
