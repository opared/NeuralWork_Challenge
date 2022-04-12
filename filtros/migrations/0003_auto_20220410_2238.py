# Generated by Django 3.0.5 on 2022-04-10 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filtros', '0002_auto_20220410_2137'),
    ]

    operations = [
        migrations.CreateModel(
            name='datos_csv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=50, verbose_name='region')),
                ('origin_coord', models.CharField(max_length=50, verbose_name='origin_coord')),
                ('destination_coord', models.CharField(max_length=50, verbose_name='destination_coord')),
                ('datetime', models.CharField(max_length=50, verbose_name='datetime')),
                ('datasource', models.CharField(max_length=50, verbose_name='datasource')),
            ],
        ),
        migrations.AlterField(
            model_name='archviajes',
            name='file',
            field=models.FileField(upload_to='data/'),
        ),
    ]