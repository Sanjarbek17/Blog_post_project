# Generated by Django 4.1.2 on 2022-10-11 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('databaseApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to='databaseApp.user'),
        ),
    ]