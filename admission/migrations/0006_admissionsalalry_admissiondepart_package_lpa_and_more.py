# Generated by Django 4.1.2 on 2022-10-28 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0005_alter_admissiondepart_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdmissionSalalry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary_ammount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.AddField(
            model_name='admissiondepart',
            name='package_lpa',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='admissiondepart',
            name='salary',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admission.admissionsalalry'),
        ),
    ]
