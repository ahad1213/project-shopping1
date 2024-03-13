# Generated by Django 4.2.11 on 2024-03-11 00:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemsHome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ItemsDetailsHome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('qty', models.IntegerField()),
                ('tax', models.FloatField()),
                ('image', models.CharField(max_length=150)),
                ('total', models.FloatField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('itemsid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Home.itemshome')),
            ],
        ),
    ]