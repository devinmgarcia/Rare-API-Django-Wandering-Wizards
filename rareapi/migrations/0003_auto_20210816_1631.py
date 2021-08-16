# Generated by Django 3.2.6 on 2021-08-16 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rareapi', '0002_auto_20210816_1553'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.AlterField(
            model_name='post',
            name='image_url',
            field=models.ImageField(null=True, upload_to='image'),
        ),
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rareapi.category')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rareapi.post')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(related_name='category', through='rareapi.PostCategory', to='rareapi.Category'),
        ),
    ]
