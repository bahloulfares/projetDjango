# Generated by Django 5.0.2 on 2024-04-12 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tache',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('termine', models.BooleanField(default=False)),
            ],
        ),
    ]