# Generated by Django 3.2.5 on 2024-02-05 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('quantity', models.FloatField(default=0.0)),
                ('customer', models.CharField(max_length=50)),
            ],
        ),
    ]
