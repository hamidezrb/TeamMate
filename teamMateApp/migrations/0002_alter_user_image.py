# Generated by Django 4.1.3 on 2022-12-07 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teamMateApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(upload_to='img'),
        ),
    ]
