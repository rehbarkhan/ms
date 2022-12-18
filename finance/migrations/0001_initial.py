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
            name='FinanceSalary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary_date', models.DateField()),
                ('salary_ammount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='FinanceDepartment',
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
                ('account_type', models.CharField(default='', max_length=255)),
                ('package_lpa', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('salary', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='finance.financesalary')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='finance', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
