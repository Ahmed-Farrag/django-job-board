# Generated by Django 4.2.1 on 2023-07-24 12:18

from django.db import migrations, models
import job.models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_job_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='image',
            field=models.ImageField(upload_to=job.models.image_upload),
        ),
        migrations.AlterField(
            model_name='job',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
