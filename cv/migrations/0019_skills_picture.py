# Generated by Django 4.2.6 on 2023-10-15 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0018_skills_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='skills',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='picture_Skills/'),
        ),
    ]
