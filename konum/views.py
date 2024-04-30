from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from konum.models import *
from konum.forms import *

@login_required(login_url='/')
def ListKonumVİew(request):
    
    konumlar = Konum.objects.all()
    search_query = request.GET.get('search')
    filtre = False
    
    if search_query:
        konumlar = konumlar.filter(ekipmanKonumu__icontains=search_query)
        filtre = True
    
    context = {'konumlar': konumlar, 'filtre': filtre}
    return render(request, "konumViews/konumIndex.html", context)



@login_required(login_url='/')
def CreateKonumView(request):
    if request.method == "POST":

        form = CreateKonumForm(request.POST)

        if form.is_valid():
            form.save()
            linkkontrol_param = request.GET.get('linkkontrol')

            if linkkontrol_param == 'True':
               return redirect('CreateEkipman')
            else:
                return redirect('KonumIndex')
    else:
        form = CreateKonumForm()
        linkkontrol_param = request.GET.get('linkkontrol')
        context = {'form' : form, 'linkkontrol_param' : linkkontrol_param}
        return render(request, 'konumViews/createKonum.html', context)

@login_required(login_url='/')
def UpdateKonumView(request, id):

    konum = get_object_or_404(Konum, id=id)
    konumlar = Konum.objects.all()
    if request.method == 'POST':
        form = UpdateKonumForm(request.POST,instance=konum)
        if form.is_valid():
            form.save()
            return redirect('KonumIndex')
    else:
        form = UpdateKonumForm()
        formId = konum.id
        context = {'form' : form, 'konumlar' : konumlar,'formId' : formId}
    return render(request,'konumViews/konumIndex.html', context)

@login_required(login_url='/')
def DeleteKonumView(request, pk):
    konum = get_object_or_404(Konum, pk=pk)
    konum.delete()
    
    return redirect('KonumIndex')
