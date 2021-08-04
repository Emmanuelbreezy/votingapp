# Generated by Django 3.2.5 on 2021-07-20 19:02

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(blank=True, max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('firstname', models.CharField(blank=True, max_length=50)),
                ('lastname', models.CharField(blank=True, max_length=50)),
                ('dob', models.DateField(blank=True)),
                ('localgovernment', models.CharField(blank=True, max_length=100)),
                ('fingerprintID', models.CharField(blank=True, max_length=100)),
                ('photo', models.ImageField(blank=True, upload_to=users.models.user_directory_path)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
