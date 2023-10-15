# Generated by Django 4.2.6 on 2023-10-15 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0006_about_cv_alter_about_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Competence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('competence_name', models.CharField(max_length=500)),
                ('competence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cv.about')),
            ],
        ),
    ]
