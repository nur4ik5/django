# Generated by Django 3.2.9 on 2021-12-25 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20211220_1905'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='post_covers/'),
        ),
    ]
