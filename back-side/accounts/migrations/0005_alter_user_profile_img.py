# Generated by Django 3.2 on 2022-11-22 15:18

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_user_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_img',
            field=imagekit.models.fields.ProcessedImageField(default='profile/download.png', upload_to='profile'),
        ),
    ]
