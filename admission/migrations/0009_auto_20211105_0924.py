# Generated by Django 3.2.8 on 2021-11-05 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0008_alter_studentinfo_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teachersinfomodel',
            name='contact_number',
        ),
        migrations.AddField(
            model_name='teachersinfomodel',
            name='contact_no',
            field=models.CharField(default='+977', max_length=15, verbose_name='Contact Number'),
        ),
    ]