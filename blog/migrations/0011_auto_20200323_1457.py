# Generated by Django 2.2.6 on 2020-03-23 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20200323_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userposts',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='blog_image'),
        ),
    ]
