# Generated by Django 3.1.1 on 2020-09-30 05:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('marvel', '0006_auto_20200930_0543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characters',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='characters',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date updated'),
        ),
        migrations.AlterField(
            model_name='usercharacters',
            name='added_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date added'),
        ),
    ]
