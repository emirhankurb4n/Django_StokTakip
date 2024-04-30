from django.db import models

class Makine(models.Model):
    makineAdi = models.CharField(max_length=50, verbose_name = "Makine Adı")

    def __str__(self) -> str:
        return self.makineAdi 
