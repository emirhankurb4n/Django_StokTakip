from django.db import models
     
class EkipmanTuru(models.Model):
     ekipmanTuru = models.CharField(max_length=50, verbose_name = "Ekipman Türü") 

     def __str__(self) -> str:
        return self.ekipmanTuru    

