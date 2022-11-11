# Generated by Django 4.1.2 on 2022-11-11 10:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('duration', models.IntegerField()),
                ('fee', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('middlename', models.CharField(blank=True, max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('date_of_birth', models.DateField()),
                ('mobile', models.CharField(max_length=10)),
                ('emergency_mobile', models.CharField(max_length=10)),
                ('present_address', models.CharField(max_length=255)),
                ('present_city', models.CharField(max_length=255)),
                ('present_state', models.CharField(max_length=255)),
                ('present_zip', models.IntegerField()),
                ('permanent_address', models.CharField(max_length=255)),
                ('permanent_city', models.CharField(max_length=255)),
                ('permanent_state', models.CharField(max_length=255)),
                ('permanent_zip', models.IntegerField()),
                ('actual_fee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course', to='student.course')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='studen_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CourseFee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('ammount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Course', to='student.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Student', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
