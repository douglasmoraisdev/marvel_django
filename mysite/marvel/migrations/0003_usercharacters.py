# Generated by Django 3.1.1 on 2020-09-30 03:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marvel', '0002_auto_20200930_0317'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCharacters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('char_user_alias', models.CharField(max_length=100)),
                ('added_at', models.DateTimeField(verbose_name='date added')),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marvel.characters')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marvel.useraccount')),
            ],
        ),
    ]
