# Generated by Django 4.0.7 on 2024-10-19 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='article',
            name='date_publication',
            field=models.DateField(auto_now_add=True),
        ),
    ]
