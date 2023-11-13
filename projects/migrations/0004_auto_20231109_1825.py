# Generated by Django 2.2 on 2023-11-09 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20231109_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='bottom_image_title',
            field=models.CharField(blank=True, help_text='(OPTIONAL) Title of projects images', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='projects',
            name='front_image_title',
            field=models.CharField(blank=True, help_text='(OPTIONAL) Title of projects images', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='projects',
            name='isometric_image_title',
            field=models.CharField(blank=True, help_text='(OPTIONAL) Title of projects images', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='projects',
            name='project_file_link',
            field=models.URLField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='projects',
            name='side_image_title',
            field=models.CharField(blank=True, help_text='(OPTIONAL) Title of projects images', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='projects',
            name='top_image_title',
            field=models.CharField(blank=True, help_text='(OPTIONAL) Title of projects images', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='projects',
            name='bottom_image',
            field=models.ImageField(blank=True, help_text='(OPTIONAL) Upload bottom view of the model.', null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='top_image',
            field=models.ImageField(blank=True, help_text='(OPTIONAL) Upload top view of the model.', null=True, upload_to='images/'),
        ),
    ]