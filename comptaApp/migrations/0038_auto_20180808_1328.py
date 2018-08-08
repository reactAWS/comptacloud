# Generated by Django 2.0.4 on 2018-08-08 13:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comptaApp', '0037_auto_20180706_1729'),
    ]

    operations = [
        migrations.CreateModel(
            name='banque',
            fields=[
                ('banqueid', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(blank=True, max_length=200, null=True)),
                ('situation', models.CharField(blank=True, max_length=200, null=True)),
                ('telephone', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='categorieimpot',
            fields=[
                ('categorieimpotid', models.AutoField(primary_key=True, serialize=False)),
                ('libelle', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='declarations',
            fields=[
                ('declarationid', models.AutoField(primary_key=True, serialize=False)),
                ('mois', models.IntegerField(blank=True, null=True)),
                ('trim', models.IntegerField(blank=True, null=True)),
                ('annee', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='impotdeclaration',
            fields=[
                ('impotdeclarationid', models.AutoField(primary_key=True, serialize=False)),
                ('montantdu', models.FloatField(blank=True, null=True)),
                ('montantregle', models.FloatField(blank=True, null=True)),
                ('declarations', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='comptaApp.declarations')),
            ],
        ),
        migrations.CreateModel(
            name='impotstaxe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(blank=True, max_length=200, null=True)),
                ('categorieimpot', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='comptaApp.categorieimpot')),
            ],
        ),
        migrations.CreateModel(
            name='reglementimpot',
            fields=[
                ('reglemenntimpotid', models.AutoField(primary_key=True, serialize=False)),
                ('nchequevirement', models.CharField(blank=True, max_length=200, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('montant', models.FloatField(blank=True, null=True)),
                ('unique', models.BooleanField(default=False)),
                ('banque', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='comptaApp.banque')),
                ('declaration', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='comptaApp.declarations')),
                ('modereglementid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='comptaApp.reglement')),
            ],
        ),
        migrations.CreateModel(
            name='serviceassiette',
            fields=[
                ('serviceassietteid', models.AutoField(primary_key=True, serialize=False)),
                ('situation', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='specialisation',
            fields=[
                ('specialisationid', models.AutoField(primary_key=True, serialize=False)),
                ('libelle', models.CharField(blank=True, max_length=200, null=True)),
                ('impots_taxe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='comptaApp.impotstaxe')),
            ],
        ),
        migrations.CreateModel(
            name='user_banque',
            fields=[
                ('user_banqueid', models.AutoField(primary_key=True, serialize=False)),
                ('gestionnaire', models.CharField(blank=True, max_length=200, null=True)),
                ('banque', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='comptaApp.banque')),
            ],
        ),
        migrations.CreateModel(
            name='usertaxe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taxeids', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='boite_postale',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='customuser',
            name='commune',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='customuser',
            name='comptecontribuable',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='customuser',
            name='ncc',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='customuser',
            name='nlot',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='nom_dirigeant',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='customuser',
            name='objet_ou_activite',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='customuser',
            name='quartier',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='customuser',
            name='raisonsociale',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='customuser',
            name='regime',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AddField(
            model_name='customuser',
            name='rue',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='customuser',
            name='sigle',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='customuser',
            name='telephone',
            field=models.CharField(blank=True, max_length=55),
        ),
        migrations.AddField(
            model_name='usertaxe',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user_banque',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='impotdeclaration',
            name='impots_taxe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='comptaApp.impotstaxe'),
        ),
        migrations.AddField(
            model_name='impotdeclaration',
            name='reglementimpot',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='comptaApp.reglementimpot'),
        ),
        migrations.AddField(
            model_name='impotdeclaration',
            name='specialisation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='comptaApp.specialisation'),
        ),
        migrations.AddField(
            model_name='declarations',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
    ]