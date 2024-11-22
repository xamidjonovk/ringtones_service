# Generated by Django 5.1.3 on 2024-11-22 05:37

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ringtones_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="ringtone",
            name="gender",
            field=models.IntegerField(choices=[(0, "Boys"), (1, "Girls")], default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="ringtone",
            name="ringtone_file",
            field=models.FileField(
                storage=django.core.files.storage.FileSystemStorage(location="media/"),
                upload_to="",
            ),
        ),
    ]