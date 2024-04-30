from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from kategori.models import *
from kategori.forms import *



@login_required(login_url='/')
def KategoriListView(request):
    kategoriler = EkipmanTuru.objects.all()
    search_query = request.GET.get('search')
    filtre = False
    
    if search_query:
        kategoriler = kategoriler.filter(ekipmanTuru__icontains=search_query)
        filtre = True

    context = {'kategoriler': kategoriler,'filtre':filtre}
    return render(request, "kategoriViews/kategoriIndex.html", context)



@login_required(login_url='/')
def KategoriCreateView(request):
    if request.method == "POST":

        form = CreateKategoriForm(request.POST)

        if form.is_valid():
            form.save()
            linkkontrol_param = request.GET.get('linkkontrol')

            if linkkontrol_param == 'True':
               return redirect('CreateEkipman')
            else:
                return redirect('KategoriIndex')
    else:
        form = CreateKategoriForm()
        linkkontrol_param = request.GET.get('linkkontrol')
        context = {'form' : form, 'linkkontrol_param' : linkkontrol_param}
        return render(request, 'kategoriViews/createKategori.html', context)
    


@login_required(login_url='/')
def KategoriUpdateView(request, id):

    kategori = get_object_or_404(EkipmanTuru, id=id)
    kategoriler = EkipmanTuru.objects.all()
    if request.method == 'POST':
        form = UpdateKategoriForm(request.POST, instance=kategori)
        if form.is_valid():
            form.save()
            return redirect('KategoriIndex')
    else:
        form = UpdateKategoriForm()
        formId = kategori.id
        context = {'form' : form, 'kategoriler' : kategoriler,'formId' : formId}
    return render(request,'kategoriViews/kategoriIndex.html', context)



@login_required(login_url='/')
def KategoriDeleteView(request, id):
    kategori = get_object_or_404(EkipmanTuru, id=id)
    kategori.delete()
    
    return redirect('KategoriIndex')