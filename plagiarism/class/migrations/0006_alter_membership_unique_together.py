# Generated by Django 4.1.7 on 2024-03-26 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('class', '0005_membership'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='membership',
            unique_together={('student', 'workspace')},
        ),
    ]