# Generated by Django 3.2.24 on 2024-02-09 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../placeholder', upload_to='images/'),
        ),
    ]
