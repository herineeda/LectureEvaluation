# Generated by Django 3.0.1 on 2020-02-21 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0015_evals'),
    ]

    operations = [
        migrations.AddField(
            model_name='evals',
            name='lect',
            field=models.ForeignKey(default=10, on_delete=django.db.models.deletion.CASCADE, to='crud.Lecture'),
            preserve_default=False,
        ),
    ]