# Generated by Django 5.0.6 on 2024-05-19 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users_data',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'users_data',
            },
        ),
    ]
