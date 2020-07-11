# Generated by Django 3.0.8 on 2020-07-10 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0010_schooluser_grades'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='students',
            field=models.ManyToManyField(blank=True, null=True, related_name='students', to='school.SchoolUser'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teacher', to='school.SchoolUser'),
        ),
    ]
