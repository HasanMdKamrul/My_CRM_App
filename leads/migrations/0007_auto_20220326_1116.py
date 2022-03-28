# Generated by Django 3.1.4 on 2022-03-26 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0006_auto_20220326_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='leads.userprofile'),
        ),
        migrations.AlterField(
            model_name='lead',
            name='organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='leads.userprofile'),
        ),
    ]