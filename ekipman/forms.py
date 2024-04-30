from django import forms
from kategori.models import EkipmanTuru
from tedarikci.models import Tedarikci
from konum.models import Konum
from ekipman.models import Ekipman, HataTalep
from makine.models import Makine
from django.forms import Textarea, CheckboxInput
from datetime import datetime

class EkipmanFiltreForm(forms.Form):
    ekipman_adi = forms.CharField(required=False, label="Ekipman Adı")
    ekipman_turu = forms.ModelChoiceField(queryset=EkipmanTuru.objects.all(), empty_label="Tümü", required=False, label="Ekipman Türü")
    ekipman_konumu = forms.ModelChoiceField(queryset=Konum.objects.all(), empty_label="Tümü", required=False, label="Ekipman Konumu")
    ekipman_markasi = forms.CharField(required=False, label="Ekipman Markası")
    tedarikci_firma = forms.ModelChoiceField(queryset=Tedarikci.objects.all(), empty_label="Tümü", required=False, label="Tedarikçi Firma")
    aktiflik_durumu = forms.BooleanField(required=False, initial=True, widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'checked': 'checked'}))
 
class AddEkipmanForm(forms.ModelForm):
    ekipmanAdi = forms.CharField()
    ekipmanAciklamasi = forms.Textarea()
    ekipmanTuru = forms.ModelChoiceField(queryset=EkipmanTuru.objects.all(), empty_label="Kategori Seçiniz")
    ekipmanKonumu = forms.ModelChoiceField(queryset=Konum.objects.all(), empty_label="Konum Seçiniz")
    ekipmanMarkasi = forms.CharField()
    ekipmanResmi = forms.ImageField( required=False, widget=forms.ClearableFileInput())
    ekipmanVarlikStokMiktari = forms.IntegerField()
    arizaliMiktar = forms.IntegerField()
    kullanilanMiktar = forms.IntegerField()
    kullanilabilirMiktar = forms.IntegerField()
    ekleyenPersonel = forms.CharField(widget=forms.TextInput(attrs={'type':'hidden','value':'user_full_name'}))
    eklenmeTarihi = forms.DateField(widget=forms.TextInput(attrs={'type':'hidden','value':'01/01/2024'}))
    iliskiliMakine = forms.ModelChoiceField(queryset=Makine.objects.all(), required=False, empty_label="Makine Seçiniz")
    tedarikciFirma = forms.ModelChoiceField(queryset=Tedarikci.objects.all(), empty_label="Tedarikçi Seçiniz")
    aktiflikDurumu = forms.BooleanField()

    class Meta:
        model = Ekipman
        fields = ('__all__')
        widgets = {
            'ekipmanAciklamasi': Textarea(attrs={'rows': 5}),  # Özelleştirilmiş textarea
        }

class AktiflikKontrolForm(forms.ModelForm):

    aktiflikDurumu = forms.CheckboxInput()

    class Meta:
       model = Ekipman
       fields = ['aktiflikDurumu']
       widgets = {
            'aktiflikDurumu': CheckboxInput()
        }
    
class EditEkipmanForm(forms.ModelForm):
    ekipmanAdi = forms.CharField()
    ekipmanAciklamasi = forms.Textarea()
    ekipmanTuru = forms.ModelChoiceField(queryset=EkipmanTuru.objects.all(), empty_label="Kategori Seçiniz")
    ekipmanKonumu = forms.ModelChoiceField(queryset=Konum.objects.all(), empty_label="Konum Seçiniz")
    ekipmanMarkasi = forms.CharField()
    ekipmanResmi = forms.ImageField(required=False, widget=forms.ClearableFileInput())
    ekipmanVarlikStokMiktari = forms.IntegerField()
    arizaliMiktar = forms.IntegerField()
    kullanilanMiktar = forms.IntegerField()
    kullanilabilirMiktar = forms.IntegerField()
    iliskiliMakine = forms.ModelChoiceField(queryset=Makine.objects.all(), required=False, empty_label="Makine Seçiniz")
    tedarikciFirma = forms.ModelChoiceField(queryset=Tedarikci.objects.all(), empty_label="Tedarikçi Seçiniz")
    sonGuncelleyenPersonel = forms.CharField(widget=forms.TextInput(attrs={'type':'hidden','value':'user_full_name'}))
    sonGuncellenmeTarihi = forms.DateField(widget=forms.TextInput(attrs={'type':'hidden','value':'01/01/2024'}))

    class Meta:
        model = Ekipman
        fields = ['ekipmanAdi','ekipmanTuru','ekipmanKonumu','ekipmanMarkasi','ekipmanResmi',
                  'ekipmanVarlikStokMiktari','arizaliMiktar','kullanilanMiktar','kullanilabilirMiktar',
                  'iliskiliMakine','tedarikciFirma','sonGuncelleyenPersonel','sonGuncellenmeTarihi',
                  'ekipmanAciklamasi']
        widgets = {
            'ekipmanAciklamasi': Textarea(attrs={ 'rows': 4}),
        }

class HataTalepForm(forms.ModelForm):
    aciklama = forms.CharField()
    cozulmeDurumu = forms.BooleanField(widget=forms.CheckboxInput(attrs={'type':'hidden'}), required=False)
    ekleyenPersonel = forms.CharField(widget=forms.TextInput(attrs={'type':'hidden'}))
    eklenmeTarihi = forms.DateField(widget=forms.TextInput(attrs={'type':'hidden'}))

    class Meta:
        model = HataTalep
        fields = ('__all__')  # Tüm alanları formda belirtin