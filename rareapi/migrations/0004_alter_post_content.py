# Generated by Django 3.2.6 on 2021-08-24 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rareapi', '0003_alter_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(),
        ),
    ]
