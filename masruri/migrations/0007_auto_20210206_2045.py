# Generated by Django 3.1.2 on 2021-02-06 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masruri', '0006_custumer_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custumer',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]
