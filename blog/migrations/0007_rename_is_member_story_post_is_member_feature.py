# Generated by Django 4.2.16 on 2024-11-08 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_is_member_story'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='is_member_story',
            new_name='is_member_feature',
        ),
    ]