# Generated by Django 2.2.6 on 2020-03-23 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20200323_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userposts',
            name='post_choice',
            field=models.TextField(default='Public', max_length=10),
        ),
    ]
