# Generated by Django 2.1.7 on 2019-03-03 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(verbose_name='text'),
        ),
    ]
