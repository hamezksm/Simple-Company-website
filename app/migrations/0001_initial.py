# Generated by Django 4.1.3 on 2022-11-22 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=15)),
                ('secondName', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=200)),
                ('productName', models.CharField(max_length=50)),
                ('quantity', models.PositiveIntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]
