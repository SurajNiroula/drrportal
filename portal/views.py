from django.shortcuts import render
from .models import Disaster, Location, Propertyloss, Humanloss, Disastertype, Animalloss,Disastergroup
from .tables import DisasterTable,LocationTable,PropertylossTable,HumanlossTable,DisastertypeTable,AnimallossTable,DisastergroupTable
from .forms import DisasterForm,LocationForm,PropertlossForm,HumanLossForm,DisasterTypeForm,AnimallossForm,DisastergroupForm
# Create your views here.


from django.shortcuts import render, redirect
from django_tables2 import RequestConfig

def DisasterView(request):
    table = DisasterTable(Disaster.objects.all())
    RequestConfig(request, paginate={'per_page': 100}).configure(table)
    return render(request, 'list.html', {
        'table': table,
        'title': 'Disaster'
    })

def edit_disaster(request, pk):
    disaster = Disaster.objects.get(pk=pk)
    if request.method == "POST":
        form = DisasterForm(request.POST, instance=professor)
        if form.is_valid():
            courprofessorse = form.save()
            return redirect('DisasterView')
    else:
        form = DisasterForm(instance=disaster)
    return render(request, 'edit.html', {'form': form, 'title': 'Edit Disaster'})

def new_disaster(request):
    if request.method == "POST":
        form = DisasterForm(request.POST)
        if form.is_valid():
            disaster = form.save()
            return redirect('DisasterView')
    else:
        form = DisasterForm()
    return render(request, 'edit.html', {'form': form, 'title':'Add Disaster'})


def LocationView(request):
    table = LocationTable(Location.objects.all())
    RequestConfig(request, paginate={'per_page': 100}).configure(table)
    return render(request, 'list.html', {
        'table': table,
        'title': 'Location'
    })
def new_location(request):
    if request.method == "POST":
        form = LocationForm(request.POST)
        if form.is_valid():
            location = form.save()
            return redirect('LocationView')
    else:
        form = LocationForm()
    return render(request, 'edit.html', {'form': form, 'title':'Add Location'})

def PropertylossView(request):
    table = PropertlossTable(Propertyloss.objects.all())
    RequestConfig(request, paginate={'per_page': 100}).configure(table)
    return render(request, 'list.html', {
        'table': table,
        'title': 'PropertyLoss'
    })

def new_propertyloss(request):
    if request.method == "POST":
        form = PropertyLossForm(request.POST)
        if form.is_valid():
            propertyloss = form.save()
            return redirect('PropertylossView')
    else:
        form = PropertlossForm()
    return render(request, 'edit.html', {'form': form, 'title':'Add Propertyloss'})


def HumanLossView(request):
    table = HumanlossTable(Humanloss.objects.all())
    RequestConfig(request, paginate={'per_page': 100}).configure(table)
    return render(request, 'list.html', {
        'table': table,
        'title': 'Humanloss'
    })

def new_Humanloss(request):
    if request.method == "POST":
        form = HumanlossForm(request.POST)
        if form.is_valid():
            humanloss = form.save()
            return redirect('HumanLossView')
    else:
        form = HumanLossForm()
    return render(request, 'edit.html', {'form': form, 'title':'Add Humanloss'})

def DisastertypeView(request):
    table = DisastertypeTable(Disastertype.objects.all())
    RequestConfig(request, paginate={'per_page': 100}).configure(table)
    return render(request, 'list.html', {
        'table': table,
        'title': 'Disastertype'
    })

def new_disastertype(request):
    if request.method == "POST":
        form = DisasterForm(request.POST)
        if form.is_valid():
            disastertype = form.save()
            return redirect('DisastertypeView')
    else:
        form = DisasterTypeForm()
    return render(request, 'edit.html', {'form': form, 'title':'Add Disastertype'})

def AnimallossView(request):
    table = AnimallossTable(Animalloss.objects.all())
    RequestConfig(request, paginate={'per_page': 100}).configure(table)
    return render(request, 'list.html', {
        'table': table,
        'title': 'Animalloss'
    })

def new_Animalloss(request):
    if request.method == "POST":
        form = AnimallossForm(request.POST)
        if form.is_valid():
            animalloss = form.save()
            return redirect('AnimallossView')
    else:
        form = DisasterForm()
    return render(request, 'edit.html', {'form': form, 'title':'Add Animalloss'})

def DisastergroupView(request):
    table = DisastergroupTable(Disastergroup.objects.all())
    RequestConfig(request, paginate={'per_page': 100}).configure(table)
    return render(request, 'list.html', {
        'table': table,
        'title': 'Disastergroup'
    })

def new_DisasterGroup(request):
    if request.method == "POST":
        form = Disastergroup(request)
        if form.is_valid():
            disastergroup = form.save()
            return redirect('DisasterGroupView')
    else:
        form = DisasterGroupForm()
    return render(request, 'edit.html', {'form': form, 'title':'Add DisasterGroup'})

