from django.db import models
from datetime import date

class Applications(models.Model):

    full_name = models.CharField(max_length = 254)
    ssn = models.CharField(max_length = 254)
    address = models.CharField(max_length = 254)
    city = models.CharField(max_length = 254)
    state = models.CharField(max_length = 254)
    zip_code = models.IntegerField()
    birth_date = models.DateField()
    drivers_license_number = models.CharField(max_length = 254)
    phone = models.CharField(max_length = 254)
    alternative_phone = models.CharField(max_length = 254, default = "", blank = True)
    email_address = models.CharField(max_length = 254)

    days_unavailable = models.CharField(max_length = 254)
    full_or_part_time = models.CharField(max_length = 254)
    day_or_night_shift = models.CharField(max_length = 254)
    hours_per_week = models.IntegerField()
    date_available_to_begin = models.DateField()
    
    have_been_employed_with_us = models.BooleanField()
    is_authorized_to_work_in_the_us = models.BooleanField()
    have_been_convicted = models.BooleanField()
    convicted_explanation = models.TextField(max_length = 1500, default = "", blank = True)
    glazier_experience = models.TextField(max_length = 1500, default = "", blank = True)

    reviewed = models.BooleanField(default = False)
    date_sent = models.DateField(default = date.today)