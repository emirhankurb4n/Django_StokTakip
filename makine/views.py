from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from makine.models import *
from makine.forms import * 

@login_required(login_url='/')
def ListMakineVİew(request):

    makineler = Makine.objects.all()
    search_query = request.GET.get('search')
    filtre = False
    
    if search_query:
        makineler = makineler.filter(makineAdi__icontains=search_query)
        filtre = True

    context = {'makineler': makineler, 'filtre': filtre}
    return render(request, "makineViews/makineIndex.html", context)



@login_required(login_url='/')
def CreateMakineView(request):
    if request.method == "POST":

        form = CreateMakineForm(request.POST)

        if form.is_valid():
            form.save()
            linkkontrol_param = request.GET.get('linkkontrol')

            if linkkontrol_param == 'True':
               return redirect('CreateEkipman')
            else:
                return redirect('MakineIndex')
    else:
        form = CreateMakineForm()
        linkkontrol_param = request.GET.get('linkkontrol')
        context = {'form' : form, 'linkkontrol_param' : linkkontrol_param}
        return render(request, 'makineViews/createMakine.html', context)
    


@login_required(login_url='/')
def UpdateMakineView(request, id):

    makine = get_object_or_404(Makine, id=id)
    makineler = Makine.objects.all()
    if request.method == 'POST':
        form = UpdateMakineForm(request.POST,instance=makine)
        if form.is_valid():
            form.save()
            return redirect('MakineIndex')
    else:
        form = UpdateMakineForm()
        formId = makine.id
        context = {'form' : form, 'makineler' : makineler,'formId' : formId}
    return render(request,'makineViews/makineIndex.html', context)



@login_required(login_url='/')
def DeleteMakineView(request, pk):
    makine = get_object_or_404(Makine, pk=pk)
    makine.delete()
    
    return redirect('MakineIndex')