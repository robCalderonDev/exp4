# Generated by Django 3.2.4 on 2021-07-06 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('valhalla', '0003_auto_20210706_0215'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='image',
        ),
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(null=True, upload_to='logos_id'),
        ),
    ]
