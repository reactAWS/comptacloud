# Generated by Django 2.0.4 on 2018-06-19 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comptaApp', '0030_auto_20180619_1040'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='saisieoccupe',
            field=models.BooleanField(default=False),
        ),
    ]
