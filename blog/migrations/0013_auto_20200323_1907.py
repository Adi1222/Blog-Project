# Generated by Django 2.2.6 on 2020-03-23 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20200323_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userposts',
            name='title',
            field=models.CharField(default='No_Post', max_length=200),
        ),
    ]
