# Generated by Django 2.0.4 on 2018-05-22 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comptaApp', '0017_delete_debit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Debit',
            fields=[
                ('iddebit', models.AutoField(primary_key=True, serialize=False)),
                ('operation_operationid', models.IntegerField()),
                ('compte_compteid', models.IntegerField()),
                ('operation_user_2_useridsaisie', models.IntegerField()),
                ('operation_user_2_useridimputer', models.IntegerField()),
                ('operation_typejournal_idtypejournal', models.PositiveIntegerField()),
                ('montant', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]