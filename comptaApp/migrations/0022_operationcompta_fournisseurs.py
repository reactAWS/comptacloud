# Generated by Django 2.0.4 on 2018-05-22 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comptaApp', '0021_typejournal'),
    ]

    operations = [
        migrations.AddField(
            model_name='operationcompta',
            name='fournisseurs',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='comptaApp.Fournisseurs'),
        ),
    ]
