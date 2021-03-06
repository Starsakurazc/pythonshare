# Generated by Django 2.1.5 on 2022-03-24 15:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, unique=True)),
                ('views', models.IntegerField(default=0)),
                ('likes', models.IntegerField(default=0)),
                ('average_rating', models.IntegerField(default=0)),
                ('link', models.URLField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('comment_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=0)),
                ('comment', models.CharField(max_length=10000)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='soundshare.Album')),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, unique=True)),
                ('link', models.URLField(unique=True)),
                ('musician_name', models.CharField(max_length=64)),
                ('album_title', models.CharField(max_length=64)),
                ('average_rating', models.IntegerField(default=0)),
                ('views', models.IntegerField(default=0)),
                ('likes', models.IntegerField(default=0)),
                ('image', models.ImageField(default='/static/image/song_photo_default.png', max_length=200, upload_to='image/', verbose_name='Music photo')),
                ('creator', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(blank=True, max_length=64)),
                ('lastname', models.CharField(blank=True, max_length=64)),
                ('type', models.CharField(choices=[('Creator', 'Creator'), ('Listener', 'Listener'), ('Producer', 'Producer')], default='Listener', max_length=10)),
                ('image', models.ImageField(default='/static/image/user_photo_default.png', max_length=200, upload_to='image/', verbose_name='Profile photo')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='feedback',
            name='song',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='soundshare.Song'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='soundshare.UserProfile'),
        ),
        migrations.AddField(
            model_name='comment',
            name='song',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='soundshare.Song'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='album',
            name='creator',
            field=models.ManyToManyField(to='soundshare.UserProfile'),
        ),
    ]
