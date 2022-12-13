# Generated by Django 4.1.3 on 2022-12-13 10:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teamMateApp', '0002_alter_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='image',
            field=models.ImageField(upload_to='D:\\Cs50_Web\\teamMate\\static/teamMateApp/img'),
        ),
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(upload_to='D:\\Cs50_Web\\teamMate\\static/teamMateApp/img'),
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fromUser', models.ManyToManyField(related_name='fromUsers', to=settings.AUTH_USER_MODEL)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teamMateApp.team')),
                ('toUser', models.ManyToManyField(related_name='toUsers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]