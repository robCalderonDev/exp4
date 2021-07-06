# Generated by Django 3.2.4 on 2021-07-06 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('valhalla', '0002_alter_producto_numeroserie'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='image',
            field=models.ImageField(null=True, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='idCategoria',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='id'),
        ),
    ]