# Generated by Django 3.2 on 2022-11-17 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(default=2, max_length=100),
            preserve_default=False,
        ),
    ]
