# Generated by Django 3.2.8 on 2021-11-01 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
        ('admission', '0007_alter_teachersinfomodel_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinfo',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='course.coursemodel'),
        ),
    ]
