# Generated by Django 4.0.2 on 2022-03-01 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0002_alter_notification_created_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='notification_type',
            field=models.CharField(choices=[('follower', 'Follower'), ('like', 'Like'), ('comment', 'Comment')], max_length=20),
        ),
    ]
