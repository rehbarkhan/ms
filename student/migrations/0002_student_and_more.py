# Generated by Django 4.1.2 on 2022-11-01 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('middle_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RenameField(
            model_name='courses',
            old_name='course_name',
            new_name='course_description',
        ),
        migrations.RemoveField(
            model_name='courses',
            name='course_fee',
        ),
    ]
