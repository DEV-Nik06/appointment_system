# Generated by Django 5.1.2 on 2024-10-10 10:07

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0005_rename_appointment_time_appointment_time_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='time',
            new_name='appointment_time',
        ),
        migrations.AlterUniqueTogether(
            name='appointment',
            unique_together={('student', 'staff', 'appointment_date', 'appointment_time')},
        ),
    ]
