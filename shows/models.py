from django.db import models

# Create your models here.

class Propagation_model(models.Model):
	Frequency = models.IntegerField() # Frequency
	Antenna_Height = models.DecimalField(max_digits = 3, decimal_places=0) # Antenna Height
	EIRP = models.DecimalField(max_digits = 3, decimal_places=0) # EIRP

