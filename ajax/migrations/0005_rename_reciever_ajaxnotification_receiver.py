# Generated by Django 4.1.1 on 2022-10-24 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ajax', '0004_alter_ajaxnotification_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ajaxnotification',
            old_name='reciever',
            new_name='receiver',
        ),
    ]
