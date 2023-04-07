# Generated by Django 4.1.7 on 2023-03-25 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Elearning', '0003_cours'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cours', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Elearning.cours')),
                ('etudiant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Elearning.etudiant')),
            ],
        ),
    ]