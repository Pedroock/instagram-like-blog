# Generated by Django 4.1.1 on 2022-10-24 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_blogposts_date'),
        ('ajax', '0003_alter_ajaxnotification_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ajaxnotification',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.blogposts'),
        ),
    ]
