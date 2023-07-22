# Generated by Django 4.2.1 on 2023-07-22 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_type',
            field=models.CharField(choices=[('Full Time', 'full time'), ('Part Time', 'Part time')], default='', max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='job',
            name='title',
            field=models.CharField(max_length=10),
        ),
    ]