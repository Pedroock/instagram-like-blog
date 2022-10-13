# Generated by Django 4.1.1 on 2022-10-13 12:26

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_usersprofile_pfp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersprofile',
            name='pfp',
            field=django_resized.forms.ResizedImageField(crop=None, default='default_pfp.png', force_format=None, keep_meta=True, quality=-1, scale=None, size=[1920, 1080], upload_to='profile_pics'),
        ),
    ]
