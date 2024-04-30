from django.db import models

class Tedarikci(models.Model):
     tedarikciFirma = models.CharField(max_length=100, verbose_name = "Tedarikçi Firma") 

     def __str__(self) -> str:
        return self.tedarikciFirma 
