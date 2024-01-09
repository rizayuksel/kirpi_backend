# Generated by Django 5.0.1 on 2024-01-09 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CandidateUserComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, null=True, verbose_name='Karavan Ismi')),
                ('is_active', models.BooleanField(default=True, verbose_name='Aktif Mi?')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Katildigi Tarih')),
            ],
        ),
    ]
