# Generated by Django 3.1 on 2020-11-05 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marvel', '0011_auto_20200930_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characters',
            name='char_external_url',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='usercharacters',
            name='char_user_alias',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
