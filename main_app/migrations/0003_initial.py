# Generated by Django 4.0.3 on 2022-03-23 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('img', models.CharField(max_length=250)),
                ('age', models.IntegerField()),
                ('attribute', models.CharField(max_length=500)),
                ('gender', models.CharField(choices=[('f', 'female'), ('m', 'male'), ('x', 'fluid')], max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]