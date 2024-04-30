from django import forms
from makine.models import Makine

class CreateMakineForm(forms.ModelForm):
    class Meta:
        model = Makine
        fields = ['makineAdi']

class UpdateMakineForm(forms.ModelForm):
    class Meta:
        model = Makine
        fields = ['makineAdi']