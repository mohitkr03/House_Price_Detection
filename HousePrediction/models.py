from django.db import models
# Create your models here.

class HouseData(models.Model):
    bedrooms = models.IntegerField()
    facing = models.CharField(max_length=10)
    club_house = models.BooleanField(default=False)
    play_area = models.BooleanField(default=False)
    water_supply = models.BooleanField(default=False)
    lift = models.BooleanField(default=False)
    nearby_hsptl_km = models.FloatField()
    parking = models.BooleanField(default=False)
    furnished = models.BooleanField(default=False)
    bathrooms = models.FloatField()
    size = models.IntegerField()
    floors = models.IntegerField()
    zipcode = models.IntegerField()
    price = models.IntegerField()
    
    def __str__(self):
        return f"House({self.bedrooms}, {self.bathrooms}, {self.size}, {self.facing}, {self.club_house}, {self.play_area}, {self.water_supply}, {self.lift}, {self.nearby_hsptl_km}, {self.parking}, {self.furnished}, {self.zipcode})"
    