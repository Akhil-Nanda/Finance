# Generated by Django 4.1.5 on 2023-04-09 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.TextField(max_length=250)),
                ('email', models.EmailField(max_length=250, unique=True)),
                ('messages', models.TextField(max_length=400)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
