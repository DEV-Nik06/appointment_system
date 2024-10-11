# Generated by Django 5.1.2 on 2024-10-10 09:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0004_rename_time_appointment_appointment_time_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='appointment_time',
            new_name='time',
        ),
        migrations.AlterUniqueTogether(
            name='appointment',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staff_appointments', to='appointments.staff'),
        ),
        migrations.AlterUniqueTogether(
            name='appointment',
            unique_together={('student', 'staff', 'appointment_date', 'time')},
        ),
    ]
