# Generated by Django 3.2.5 on 2021-08-04 15:04

from django.db import migrations, models
import elections.models


class Migration(migrations.Migration):

    dependencies = [
        ('elections', '0006_alter_vote_candidate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='candidate_img',
            field=models.ImageField(blank=True, max_length=250, upload_to=elections.models.user_cand_path),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='candidate_name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='posted_by',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='election',
            name='cover_img',
            field=models.ImageField(blank=True, max_length=250, upload_to=elections.models.user_dir_path),
        ),
        migrations.AlterField(
            model_name='election',
            name='election_name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='election',
            name='posted_by',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='election',
            name='url_extid',
            field=models.SlugField(blank=True, max_length=250, unique=True),
        ),
    ]
