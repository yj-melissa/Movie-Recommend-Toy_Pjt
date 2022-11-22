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
            name='Movie',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('overview', models.TextField()),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('genre_ids', models.JSONField()),
                ('adult', models.BooleanField()),
                ('backdrop_path', models.TextField(null=True)),
                ('original_language', models.TextField()),
                ('popularity', models.IntegerField()),
                ('poster_path', models.TextField(null=True)),
                ('release_date', models.TextField()),
                ('vote_average', models.FloatField()),
                ('actors', models.JSONField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SortedMovie',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('genre_ids', models.JSONField()),
                ('poster_path', models.TextField(null=True)),
                ('release_date', models.TextField()),
                ('actors', models.JSONField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=50)),
                ('score', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servers.movie')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
