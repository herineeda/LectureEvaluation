# Generated by Django 3.0.1 on 2020-02-21 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0010_auto_20200221_1503'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eval',
            name='texts',
        ),
    ]
