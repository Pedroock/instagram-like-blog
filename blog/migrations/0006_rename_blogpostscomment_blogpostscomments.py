# Generated by Django 4.0.6 on 2022-10-06 23:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_usersprofile_pfp'),
        ('blog', '0005_alter_blogposts_date_blogpostscomment'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BlogPostsComment',
            new_name='BlogPostsComments',
        ),
    ]
