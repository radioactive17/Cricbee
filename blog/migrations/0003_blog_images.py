# Generated by Django 4.0.2 on 2022-03-09 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='images',
            field=models.ImageField(default='default_blog.html', upload_to='blog/'),
        ),
    ]
