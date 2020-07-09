# Generated by Django 3.0.8 on 2020-07-08 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0008_auto_20200706_1947'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answer_right', models.CharField(max_length=150)),
                ('answer_1_wrong', models.CharField(max_length=150)),
                ('answer_2_wrong', models.CharField(max_length=150)),
                ('answer_3_wrong', models.CharField(max_length=150)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='school.SchoolUser')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Lesson')),
            ],
        ),
    ]