# Generated by Django 4.2.2 on 2023-06-23 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0002_marca'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
    ]
