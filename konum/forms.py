from django import forms
from konum.models import *

class CreateKonumForm(forms.ModelForm):
    class Meta:
        model = Konum
        fields = ['ekipmanKonumu']

class UpdateKonumForm(forms.ModelForm):
    class Meta:
        model = Konum
        fields = ['ekipmanKonumu']