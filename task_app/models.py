from django.db import models
from geopy.geocoders import Nominatim

# Create your models here.

class Cities(models.Model):
    city = models.CharField(max_length=50)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)


    def __str__(self):
        return self.city


    def save(self, *args, **kwargs):
        # calling the Nominatim tool and create Nominatim class
        loc = Nominatim(user_agent="Geopy Library")

        # entering the location name
        getLoc = loc.geocode(self.city)

        # printing address
        print(getLoc.address)
        self.latitude = getLoc.latitude
        self.longitude = getLoc.longitude
        # printing latitude and longitude
        print("Latitude = ", getLoc.latitude)
        print("Longitude = ", getLoc.longitude)
        super().save(*args, **kwargs)

