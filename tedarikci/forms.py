from django import forms
from tedarikci.models import *

class CreateTedarikciForm(forms.ModelForm):
    class Meta:
        model = Tedarikci
        fields = ['tedarikciFirma']

class UpdateTedarikciForm(forms.ModelForm):
    class Meta:
        model = Tedarikci
        fields = ['tedarikciFirma']