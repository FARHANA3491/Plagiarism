# Generated by Django 4.1.7 on 2024-03-26 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('class', '0006_alter_membership_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='workspace',
            name='students',
            field=models.ManyToManyField(related_name='workspaces', through='class.Membership', to='profiles.student'),
        ),
    ]