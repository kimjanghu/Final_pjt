# Generated by Django 2.1.15 on 2020-06-14 04:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='user',
        ),
        migrations.AddField(
            model_name='review',
            name='scored_users',
            field=models.ManyToManyField(related_name='scored_reviews', to=settings.AUTH_USER_MODEL),
        ),
    ]
