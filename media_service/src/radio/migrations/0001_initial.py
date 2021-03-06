# Generated by Django 4.0.6 on 2022-07-07 07:11

from django.db import migrations, models
import radio.models
import radio.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Radio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_name', models.CharField(default='Unknown_radio', max_length=100)),
                ('station_frequency', models.FloatField(default=0)),
                ('station_url', models.CharField(default='', max_length=1023)),
                ('station_cover', models.FileField(upload_to=radio.models.radio_cover_images, validators=[radio.validators.validate_image_extension])),
                ('station_description', models.TextField(blank=True, max_length=1023, null=True)),
                ('user_id', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Radio',
                'verbose_name_plural': 'Radios',
                'ordering': ['id'],
            },
        ),
    ]
