# Generated by Django 4.1.1 on 2022-10-24 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_usersprofile_pfp'),
        ('blog', '0009_alter_blogposts_date'),
        ('ajax', '0005_rename_reciever_ajaxnotification_receiver'),
    ]

    operations = [
        migrations.AddField(
            model_name='ajaxnotification',
            name='comment_obj',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.blogpostscomments'),
        ),
        migrations.AddField(
            model_name='ajaxnotification',
            name='follow_obj',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.usersfollowers'),
        ),
        migrations.AddField(
            model_name='ajaxnotification',
            name='like_obj',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.blogpostslikes'),
        ),
    ]
