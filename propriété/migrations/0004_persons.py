# Generated by Django 4.1.5 on 2023-02-19 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propriété', '0003_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Persons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idvalue', models.CharField(max_length=100)),
                ('fist_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
