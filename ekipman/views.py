from django.shortcuts import render, redirect, get_object_or_404
from ekipman.models import Ekipman
from .forms import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from datetime import datetime
from django.urls import reverse
import os
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages





@login_required(login_url='/')
def EkipmanIndex(request):
    ekipmanlar = Ekipman.objects.all()
    filtre = False
    sayac = 0

    if request.method == 'POST':

        if 'form_submit' in request.POST:
            form = EkipmanFiltreForm(request.POST)
            if form.is_valid():
                ekipman_adi = form.cleaned_data.get('ekipman_adi')
                ekipman_turu = form.cleaned_data.get('ekipman_turu')
                ekipman_konumu = form.cleaned_data.get('ekipman_konumu')
                ekipman_markasi = form.cleaned_data.get('ekipman_markasi')
                tedarikci_firma = form.cleaned_data.get('tedarikci_firma')
                aktiflik_durumu = form.cleaned_data.get('aktiflik_durumu')
        
                if ekipman_adi:
                    ekipmanlar = ekipmanlar.filter(ekipmanAdi__icontains=ekipman_adi)
                    filtre = True
                if ekipman_turu:
                    ekipmanlar = ekipmanlar.filter(ekipmanTuru=ekipman_turu)
                    filtre = True
                if ekipman_konumu:
                    ekipmanlar = ekipmanlar.filter(ekipmanKonumu=ekipman_konumu)
                    filtre = True
                if ekipman_markasi:
                    ekipmanlar = ekipmanlar.filter(ekipmanMarkasi__icontains=ekipman_markasi)
                    filtre = True
                if tedarikci_firma:
                    ekipmanlar = ekipmanlar.filter(tedarikciFirma=tedarikci_firma)
                    filtre = True
                if aktiflik_durumu is not None:
                    ekipmanlar = ekipmanlar.filter(aktiflikDurumu=aktiflik_durumu)
                    filtre = True
            context = {'ekipmanlar' : ekipmanlar, 'form' : form, 'filtre' : filtre}
            return render(request, "ekipmanViews/ekipmanIndex.html", context)
        
        if 'form1_submit' in request.POST:
            form1 = HataTalepForm(request.POST)

            if form1.is_valid():

                form1.save()   

                subject = form1.cleaned_data['ekleyenPersonel'] + ' isimli Personel Tarafından iletilen hata talebi.'
                message = form1.cleaned_data['aciklama']
                from_email = settings.EMAIL_HOST_USER
                recipient_list = ['emirhankurban06@gmail.com']

                print(subject)
                print(message)
                print(from_email)
                print(recipient_list)

                send_mail(subject, message, from_email, recipient_list)   
                print('E-posta Başarıyla Gönderildi.')
                messages.success(request, 'E-Mail Başarı ile Gönderildi.')
            return redirect('Home')        
    
    else:
        search_query = request.GET.get('search')
        form = EkipmanFiltreForm(request.GET)

        form1 = HataTalepForm()
        form1.fields['ekleyenPersonel'].initial = request.user.get_full_name()
        now = datetime.now()
        form1.fields['eklenmeTarihi'].initial = now.strftime('%d/%m/%Y')
        form1.fields['cozulmeDurumu'].initial = False

        # Ekipman adına göre filtreleme
        if search_query:
            filtre = True
            ekipmanlar = ekipmanlar.filter(ekipmanAdi__icontains=search_query)
            

        sirala_param = request.GET.get('sirala')
        print(filtre)
        
        if sirala_param == 'id' and filtre == False:
            sayac = 1
            ekipmanlar = ekipmanlar.order_by('id')
        elif(sirala_param == 'id_ters' and filtre == False):
            sayac = 0
            ekipmanlar = ekipmanlar.order_by('-id')
            
        if sirala_param == 'ekipmanAdi' and filtre == False:
            sayac = 1
            ekipmanlar = ekipmanlar.order_by('ekipmanAdi')
        elif(sirala_param == 'ekipmanAdi_ters' and filtre == False):
            sayac = 0
            ekipmanlar = ekipmanlar.order_by('-ekipmanAdi')

        if sirala_param == 'ekipmanTuru' and filtre == False:
            sayac = 1
            ekipmanlar = ekipmanlar.order_by('ekipmanTuru')
        elif(sirala_param == 'ekipmanTuru_ters' and filtre == False):
            sayac = 0
            ekipmanlar = ekipmanlar.order_by('-ekipmanTuru')

        if sirala_param == 'ekipmanKonumu' and filtre == False:
            sayac = 1
            ekipmanlar = ekipmanlar.order_by('ekipmanKonumu')
        elif(sirala_param == 'ekipmanKonumu_ters' and filtre == False):
            sayac = 0
            ekipmanlar = ekipmanlar.order_by('-ekipmanKonumu')

        if sirala_param == 'eklenmeTarihi' and filtre == False:
            sayac = 1
            ekipmanlar = ekipmanlar.order_by('-eklenmeTarihi')
        elif(sirala_param == 'eklenmeTarihi_ters' and filtre == False):
            sayac = 0
            ekipmanlar = ekipmanlar.order_by('eklenmeTarihi')

        if sirala_param == 'aktiflikDurumu' and filtre == False:
            sayac = 1
            ekipmanlar = ekipmanlar.order_by('-aktiflikDurumu')
        elif(sirala_param == 'aktiflikDurumu_ters' and filtre == False):
            sayac = 0
            ekipmanlar = ekipmanlar.order_by('aktiflikDurumu')
        
        sayac = sayac % 2
        
        context = {'ekipmanlar' : ekipmanlar, 'form' : form, 'form1' : form1, 'filtre' : filtre, 'sayac' : sayac}
        return render(request, "ekipmanViews/ekipmanIndex.html", context)
    
  



@login_required(login_url='/')
def EkipmanCreateView(request):
    if request.method == "POST":

        form = AddEkipmanForm(request.POST, request._files)

        if form.is_valid():

            updatedForm = form.save(commit=False)
            updatedForm.eklenmeTarihi = datetime.now()
            updatedForm.ekleyenPersonel = request.user.get_full_name()
            arizaliMiktar = form.cleaned_data['arizaliMiktar']
            kullanilanMiktar = form.cleaned_data['kullanilanMiktar']
            kullanilabilirMiktar = form.cleaned_data['kullanilabilirMiktar']
            updatedForm.ekipmanVarlikStokMiktari = arizaliMiktar + kullanilanMiktar + kullanilabilirMiktar

            if updatedForm.ekipmanVarlikStokMiktari == 0:
                return render(request, 'ekipmanViews/createEkipman.html', {'form' : 
                form, "error": "Ekipmanın tüm stok miktarları 0 olamaz."})
            
            updatedForm.save()

            return redirect("/home")
        
    else:
        form = AddEkipmanForm()  
    return render(request, 'ekipmanViews/createEkipman.html', {'form' : form})





@method_decorator(login_required(login_url = '/'), name='dispatch')
class EkipmanDetailsView(DetailView):
    model = Ekipman
    template_name = "ekipmanViews/detailsEkipman.html"
    context_object_name = 'ekipman'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AktiflikKontrolForm(instance=self.object)
        ekipman_id = self.kwargs.get('pk')  # Ekipman ID'sini alın
        context['ekipman_id'] = ekipman_id
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = AktiflikKontrolForm(request.POST, instance=self.object)
        if form.is_valid():
            form.save()
            return redirect(reverse('EkipmanDetails', kwargs={'pk': self.object.id}) + '?message=Değişiklik+Başarıyla+Kaydedildi.')
        return render(request, self.template_name, {'form': form})





@login_required(login_url='/')
def EkipmanUpdateView(request, id):
    ekipman = get_object_or_404(Ekipman, id = id)
    
    if request.method == "POST":  

        if request.FILES and ekipman.ekipmanResmi:
            file_path = ekipman.ekipmanResmi.path
            if os.path.exists(file_path):
                os.remove(file_path)

        form = EditEkipmanForm(request.POST, request.FILES, instance=ekipman)  

        if form.is_valid():

            updatedEkipman = form.save(commit=False)

            updatedEkipman.ekipmanVarlikStokMiktari = updatedEkipman.arizaliMiktar + updatedEkipman.kullanilanMiktar + updatedEkipman.kullanilabilirMiktar

            if updatedEkipman.ekipmanVarlikStokMiktari == 0:
                updatedEkipman.arizaliMiktar = ekipman.arizaliMiktar
                updatedEkipman.kullanilanMiktar = ekipman.kullanilanMiktar
                updatedEkipman.kullanilabilirMiktar = ekipman.kullanilabilirMiktar
                updatedEkipman.ekipmanVarlikStokMiktari = ekipman.ekipmanVarlikStokMiktari
                return render(request, 'ekipmanViews/editEkipman.html', {'form' : form, 'ekipman' : ekipman, "error" : "Ekipmanın tüm stok miktarları 0 olamaz."})

            updatedEkipman.sonGuncelleyenPersonel = request.user.get_full_name()
            updatedEkipman.sonGuncellenmeTarihi = datetime.now()

            updatedEkipman.save()

            return redirect('EkipmanDetails', ekipman.id)
    else:
        form = EditEkipmanForm(instance=ekipman)  
    return render(request, 'ekipmanViews/editEkipman.html', {'form' : form, 'ekipman' : ekipman})





@login_required(login_url='/')
def EkipmanDeleteView(request, pk):
    ekipman = get_object_or_404(Ekipman, pk=pk)
    if ekipman.ekipmanResmi:
        os.remove(ekipman.ekipmanResmi.path)
    ekipman.delete()
    
    return redirect('/home')