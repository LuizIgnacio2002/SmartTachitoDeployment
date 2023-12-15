# Generated by Django 4.2.6 on 2023-12-15 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Detection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date and time of detection')),
                ('frame', models.ImageField(null=True, upload_to='frames/')),
                ('frame_image_detected', models.ImageField(blank=True, null=True, upload_to='frames/')),
                ('latitude', models.CharField(max_length=15, null=True)),
                ('longitude', models.CharField(max_length=15, null=True)),
                ('most_confident_label', models.CharField(blank=True, max_length=50, null=True)),
                ('confidence', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
