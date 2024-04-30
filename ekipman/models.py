from django.db import models
from kategori import models as ekipmanTuru
from konum import models as konum
from tedarikci import models as tedarikci
from makine import models as makine


class Ekipman(models.Model):
    ekipmanAdi = models.CharField(max_length=50, verbose_name = "Ekipman Adı")
    ekipmanAciklamasi = models.CharField(max_length=500, verbose_name="Ekipman Açıklaması", blank=True, null=True)
    ekipmanTuru = models.ForeignKey(ekipmanTuru.EkipmanTuru, on_delete=models.CASCADE)
    ekipmanKonumu = models.ForeignKey(konum.Konum, on_delete=models.CASCADE)
    ekipmanMarkasi = models.CharField(max_length=50, verbose_name = "Ekipmanın Markası")
    ekipmanResmi = models.ImageField(blank=True, null=True, verbose_name = "Ekipmanın Resmi")
    ekipmanVarlikStokMiktari = models.IntegerField(verbose_name = "Ekipman Varlık Stoğu")
    arizaliMiktar = models.IntegerField(verbose_name = "Arızalı Ekipman Stoğu")
    kullanilanMiktar = models.IntegerField(verbose_name = "Aktif Ekipman Stoğu")
    kullanilabilirMiktar = models.IntegerField(verbose_name = "Erişilebilir Ekipman Stoğu")
    ekleyenPersonel = models.CharField(max_length=50, verbose_name = "Ekleyen Personel")
    eklenmeTarihi = models.DateField(verbose_name = "Eklenme Tarihi")
    iliskiliMakine = models.ForeignKey(makine.Makine, on_delete=models.CASCADE, null=True, blank=True)
    tedarikciFirma = models.ForeignKey(tedarikci.Tedarikci, on_delete=models.CASCADE)   
    sonGuncelleyenPersonel = models.CharField(blank=True, null=True, max_length=50, verbose_name = "Son Güncelleyen Personel")
    sonGuncellenmeTarihi = models.DateField(blank=True, null=True, verbose_name = "Son Güncellenme Tarihi")
    aktiflikDurumu = models.BooleanField(verbose_name="Aktiflik Durumu", default=True)

    def __str__(self) -> str:
         return self.ekipmanAdi

class HataTalep(models.Model):
    aciklama = models.CharField(max_length=500, verbose_name="Açıklama", null=True, blank=True)
    cozulmeDurumu = models.BooleanField(verbose_name="Çözülme Durumu", default=False)
    eklenmeTarihi = models.DateField(verbose_name="Eklenme Tarihi")
    ekleyenPersonel = models.CharField(max_length=50, verbose_name="Ekleyen Personel")  # Dış anahtar olarak değil, doğrudan bir metin alanı

    def __str__(self) -> str:
        return self.ekleyenPersonel + ' isimli Personel Tarafından İletildi'
