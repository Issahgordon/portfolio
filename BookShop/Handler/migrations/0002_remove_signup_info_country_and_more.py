# Generated by Django 4.1.3 on 2023-06-08 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Handler', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup_info',
            name='Country',
        ),
        migrations.RemoveField(
            model_name='signup_info',
            name='Last_Seen',
        ),
        migrations.RemoveField(
            model_name='signup_info',
            name='Plans',
        ),
        migrations.RemoveField(
            model_name='signup_info',
            name='Statuse',
        ),
        migrations.RemoveField(
            model_name='signup_info',
            name='Verify',
        ),
        migrations.AddField(
            model_name='signup_info',
            name='Full_Name',
            field=models.EmailField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='signup_info',
            name='Contact',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='signup_info',
            name='Location',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
