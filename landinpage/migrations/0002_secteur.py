# Generated by Django 3.0.14 on 2021-06-04 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landinpage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Secteur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
    ]
