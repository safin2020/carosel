# Generated by Django 3.2.5 on 2021-07-12 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CaroselModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100)),
                ('thumbnail', models.ImageField(upload_to='carosel_image/')),
                ('short_discription', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('thumbnail', models.ImageField(upload_to='carousel/images/')),
                ('short_discription', models.TextField()),
                ('discription', models.TextField()),
                ('creation', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]