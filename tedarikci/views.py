from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from tedarikci.models import *
from tedarikci.forms import *

@login_required(login_url='/')
def ListTedarikciVİew(request):

    tedarikciler = Tedarikci.objects.all()
    search_query = request.GET.get('search')
    filtre = False
    
    if search_query:
        tedarikciler = tedarikciler.filter(tedarikciFirma__icontains=search_query)
        filtre = True
    
    context = {'tedarikciler': tedarikciler, 'filtre': filtre}
    return render(request, "tedarikciViews/tedarikciIndex.html", context)



@login_required(login_url='/')
def CreateTedarikciView(request):
    if request.method == "POST":

        form = CreateTedarikciForm(request.POST)

        if form.is_valid():
            form.save()
            linkkontrol_param = request.GET.get('linkkontrol')

            if linkkontrol_param == 'True':
               return redirect('CreateEkipman')
            else:
                return redirect('TedarikciIndex')
    else:
        form = CreateTedarikciForm()
        linkkontrol_param = request.GET.get('linkkontrol')
        context = {'form' : form, 'linkkontrol_param' : linkkontrol_param}
        return render(request, 'tedarikciViews/createTedarikci.html', context)
    


@login_required(login_url='/')
def UpdateTedarikciView(request, id):

    tedarikci = get_object_or_404(Tedarikci, id=id)
    tedarikciler = Tedarikci.objects.all()
    if request.method == 'POST':
        form = UpdateTedarikciForm(request.POST,instance=tedarikci)
        if form.is_valid():
            form.save()
            return redirect('TedarikciIndex')
    else:
        form = UpdateTedarikciForm()
        formId = tedarikci.id
        context = {'form' : form, 'tedarikciler' : tedarikciler,'formId' : formId}
    return render(request,'tedarikciViews/tedarikciIndex.html', context)



@login_required(login_url='/')
def DeleteTedarikciView(request, pk):
    tedarikci = get_object_or_404(Tedarikci, pk=pk)
    tedarikci.delete()
    
    return redirect('TedarikciIndex')