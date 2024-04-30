from django.db import models

class Konum(models.Model):
     ekipmanKonumu = models.CharField(max_length=50, verbose_name = "Ekipmanın Konumu")  

     def __str__(self) -> str:
        return self.ekipmanKonumu 
