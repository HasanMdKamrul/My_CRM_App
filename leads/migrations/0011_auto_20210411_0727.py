# Generated by Django 3.1.4 on 2021-04-11 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0010_auto_20210411_0726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='catagory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='leads', to='leads.catagory'),
        ),
    ]
