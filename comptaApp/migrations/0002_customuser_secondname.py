# Generated by Django 2.0.4 on 2018-04-18 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comptaApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='secondname',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]