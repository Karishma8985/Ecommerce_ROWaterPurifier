# Generated by Django 5.0.3 on 2024-03-20 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ROApp', '0002_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='pics',
            field=models.ImageField(default=1, upload_to='servicesimage'),
            preserve_default=False,
        ),
    ]