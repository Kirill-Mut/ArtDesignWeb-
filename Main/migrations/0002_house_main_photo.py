# Generated by Django 5.1.1 on 2024-09-18 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='main_photo',
            field=models.ImageField(default='Main\\static\\images\tq__iesr2jwby-x1cp-1500h.png', upload_to='main_photos/'),
        ),
    ]
