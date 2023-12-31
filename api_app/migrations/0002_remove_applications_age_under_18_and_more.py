# Generated by Django 4.0 on 2023-11-01 18:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applications',
            name='age_under_18',
        ),
        migrations.RemoveField(
            model_name='applications',
            name='begin_date',
        ),
        migrations.RemoveField(
            model_name='applications',
            name='city_state_zipcode',
        ),
        migrations.RemoveField(
            model_name='applications',
            name='drivers_license_state',
        ),
        migrations.RemoveField(
            model_name='applications',
            name='email',
        ),
        migrations.RemoveField(
            model_name='applications',
            name='has_drivers_license',
        ),
        migrations.RemoveField(
            model_name='applications',
            name='hours_available',
        ),
        migrations.RemoveField(
            model_name='applications',
            name='hours_weekly',
        ),
        migrations.RemoveField(
            model_name='applications',
            name='job_time',
        ),
        migrations.RemoveField(
            model_name='applications',
            name='mailing_address',
        ),
        migrations.RemoveField(
            model_name='applications',
            name='night_working',
        ),
        migrations.RemoveField(
            model_name='applications',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='applications',
            name='social_security_number',
        ),
        migrations.RemoveField(
            model_name='applications',
            name='us_citizen',
        ),
        migrations.AddField(
            model_name='applications',
            name='address',
            field=models.CharField(default=django.utils.timezone.now, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='applications',
            name='birth_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='applications',
            name='city',
            field=models.CharField(default=django.utils.timezone.now, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='applications',
            name='convicted_explanation',
            field=models.TextField(default='', max_length=1500),
        ),
        migrations.AddField(
            model_name='applications',
            name='date_available_to_begin',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='applications',
            name='day_or_night_shift',
            field=models.CharField(default='ss', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='applications',
            name='days_unavailable',
            field=models.CharField(default='have no preference', max_length=254),
        ),
        migrations.AddField(
            model_name='applications',
            name='email_address',
            field=models.CharField(default='ss', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='applications',
            name='full_or_part_time',
            field=models.CharField(default='dd', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='applications',
            name='glazier_experience',
            field=models.TextField(default='', max_length=1500),
        ),
        migrations.AddField(
            model_name='applications',
            name='hours_per_week',
            field=models.IntegerField(default=123),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='applications',
            name='is_authorized_to_work_in_the_us',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='applications',
            name='phone',
            field=models.CharField(default='dd', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='applications',
            name='ssn',
            field=models.CharField(default='dd', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='applications',
            name='state',
            field=models.CharField(default='ee', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='applications',
            name='zip_code',
            field=models.IntegerField(default=3215),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='applications',
            name='alternative_phone',
            field=models.CharField(default='', max_length=254),
        ),
    ]
