# Generated by Django 4.1.5 on 2023-03-22 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mychatapp', '0002_friend_frofile_friends'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frofile',
            name='friends',
            field=models.ManyToManyField(blank=True, null=True, related_name='my_friends', to='mychatapp.friend'),
        ),
    ]
