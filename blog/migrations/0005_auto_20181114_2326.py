# Generated by Django 2.1.1 on 2018-11-15 01:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_writer'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'permissions': (('can_delete_posts', 'Manage posts as needed'),)},
        ),
    ]
