# Generated by Django 2.2 on 2023-11-08 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20231108_2027'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='linked_link',
            new_name='linkedin_link',
        ),
    ]
