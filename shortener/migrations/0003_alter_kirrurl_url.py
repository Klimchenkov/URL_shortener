# Generated by Django 4.0.3 on 2022-03-29 19:30

from django.db import migrations, models
import shortener.validators


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_kirrurl_active_alter_kirrurl_shortcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kirrurl',
            name='url',
            field=models.CharField(max_length=220, validators=[shortener.validators.validate_url]),
        ),
    ]
