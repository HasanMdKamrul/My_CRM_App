# Generated by Django 3.1.4 on 2021-04-13 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0012_auto_20210413_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='description',
            field=models.TextField(max_length=50),
        ),
    ]
