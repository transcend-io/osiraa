# Generated by Django 3.2.12 on 2023-04-13 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('covered_business', '0017_remove_coveredbusiness_decode_api_secret'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coveredbusiness',
            name='api_endpoint',
        ),
    ]
