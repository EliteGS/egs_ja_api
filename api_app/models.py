from django.db import models
from datetime import date

class Applications(models.Model):
    full_name = models.CharField(max_length= 254)
    social_security_number = models.IntegerField()
    mailing_address = models.CharField(max_length=254)
    city = models.CharField(max_length=254)
    state = models.CharField(max_length=2)
    zip_code = models.IntegerField()
    phone_number = models.IntegerField()
    alternative_phone = models.IntegerField()
    age = models.IntegerField()
    email = models.EmailField(max_length=254)

    hours_available = models.JSONField()
    job_time = models.CharField(max_length=254)
    hours_weekly = models.IntegerField()
    night_working = models.BooleanField()
    begin_date = models.DateField()

    have_been_employed_with_us = models.BooleanField()
    us_citizen = models.BooleanField()
    have_been_convicted = models.BooleanField()
    convicted_explain = models.TextField
    has_drivers_license = models.BooleanField()
    drivers_license_number = models.CharField(max_length=254)
    drivers_license_state = models.CharField(max_length=254)

    reviewed = models.BooleanField(default=False)
    date_sent = models.DateField(default = date.today)
