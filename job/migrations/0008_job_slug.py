# Generated by Django 4.2.1 on 2023-07-24 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0007_alter_job_image_alter_job_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]