# Generated by Django 3.1.1 on 2020-09-30 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marvel', '0003_usercharacters'),
    ]

    operations = [
        migrations.AddField(
            model_name='characters',
            name='char_external_id',
            field=models.IntegerField(default=0),
        ),
    ]
