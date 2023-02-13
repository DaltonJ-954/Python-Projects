# Generated by Django 4.1.6 on 2023-02-13 02:13

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UniversityCampus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Campus_ID', models.IntegerField(blank=True, default='')),
                ('Campus_Name', models.CharField(blank=True, default='', max_length=60)),
                ('State', models.CharField(blank=True, default='', max_length=2)),
            ],
            options={
                'verbose_name_plural': 'University Campus',
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]