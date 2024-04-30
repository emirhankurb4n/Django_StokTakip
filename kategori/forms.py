from django import forms
from kategori.models import *

class CreateKategoriForm(forms.ModelForm):
    class Meta:
        model = EkipmanTuru
        fields = ['ekipmanTuru']

class UpdateKategoriForm(forms.ModelForm):
    class Meta:
        model = EkipmanTuru
        fields = ['ekipmanTuru']