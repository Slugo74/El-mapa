# Generated by Django 3.0.5 on 2020-05-22 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cells',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('y', models.CharField(max_length=10)),
                ('x', models.CharField(max_length=10)),
                ('color', models.CharField(max_length=20)),
                ('borde', models.CharField(max_length=2)),
            ],
        ),
    ]
