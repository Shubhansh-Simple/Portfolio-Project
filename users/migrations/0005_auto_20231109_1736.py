# Generated by Django 2.2 on 2023-11-09 12:06

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20231108_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.CharField(blank=True, help_text='for eg. 7859499938', max_length=10, null=True, validators=[users.models.validate_phone], verbose_name='Mobile Number'),
        ),
    ]
