# Generated by Django 4.1.3 on 2023-06-09 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Handler', '0003_alter_signup_info_full_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User', models.IntegerField()),
                ('Category', models.CharField(max_length=100)),
                ('Name', models.CharField(max_length=100)),
                ('Rate', models.CharField(max_length=100)),
                ('About', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]