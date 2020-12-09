# Generated by Django 3.1.3 on 2020-12-07 06:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0003_post_likes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, max_length=100)),
                ('url', models.CharField(blank=True, max_length=100, null=True)),
                ('portfolio', models.TextField(blank=True, max_length=500, null=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('favourite', models.ManyToManyField(to='posts.Post')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
