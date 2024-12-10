# Generated by Django 5.1.2 on 2024-10-15 11:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('demandes', '0002_remove_demande_collaborateur_delete_collaborateur_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Departement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Collaborateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenoms', models.CharField(max_length=100)),
                ('poste', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('departement', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='demandes.departement')),
            ],
        ),
        migrations.CreateModel(
            name='Demande',
            fields=[
                ('reference', models.AutoField(primary_key=True, serialize=False)),
                ('date_demande', models.DateField(auto_now_add=True)),
                ('motif', models.TextField(blank=True, null=True)),
                ('periode_conge_debut', models.DateField(blank=True, null=True)),
                ('periode_conge_fin', models.DateField(blank=True, null=True)),
                ('date_reprise_service', models.DateField(blank=True, null=True)),
                ('lieu_mission', models.CharField(blank=True, max_length=100, null=True)),
                ('objet_mission', models.CharField(blank=True, max_length=200, null=True)),
                ('lettre_invitation', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('billet', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('tableau_amortissement', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('banque', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='demandes.banque')),
                ('collaborateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demandes.collaborateur')),
                ('document', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='demandes.document')),
            ],
        ),
    ]
