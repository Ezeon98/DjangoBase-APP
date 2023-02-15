# Generated by Django 3.2.13 on 2023-02-15 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('volume', models.FloatField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
