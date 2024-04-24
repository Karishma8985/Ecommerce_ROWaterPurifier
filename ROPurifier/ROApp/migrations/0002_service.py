# Generated by Django 5.0.3 on 2024-03-20 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ROApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('duration_months', models.IntegerField(help_text='Duration in months')),
            ],
        ),
    ]