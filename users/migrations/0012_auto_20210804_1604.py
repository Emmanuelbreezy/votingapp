# Generated by Django 3.2.5 on 2021-08-04 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dob',
            field=models.DateField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='profile',
            name='fingerprintID',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='profile',
            name='firstname',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='profile',
            name='lastname',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='profile',
            name='localgovernment',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='profile',
            name='surname',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='profile',
            name='token',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=150),
        ),
    ]