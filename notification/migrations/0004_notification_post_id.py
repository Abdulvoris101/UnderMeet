# Generated by Django 4.0.2 on 2022-03-01 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0003_alter_notification_notification_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='post_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
