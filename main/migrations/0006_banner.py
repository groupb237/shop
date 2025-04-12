# Generated by Django 5.2 on 2025-04-05 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_recentview'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='banner/%Y-%m-%d')),
                ('description', models.TextField()),
                ('added_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'banners',
                'ordering': ['-added_at'],
            },
        ),
    ]
