# Generated by Django 3.1.4 on 2021-05-31 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0013_auto_20210413_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pictures/'),
        ),
    ]
