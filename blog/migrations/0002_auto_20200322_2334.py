# Generated by Django 2.2.6 on 2020-03-22 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='post_choice',
            field=models.CharField(choices=[('PUB', 'Public'), ('PRI', 'Private')], default='Public', max_length=5),
        ),
    ]
