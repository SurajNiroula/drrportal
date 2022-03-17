import django_tables2 as tables
from django_tables2.utils import A
from .models import Disaster, Location, Propertyloss, Humanloss, Disastertype, Animalloss,Disastergroup

class DisasterTable(tables.Table):
    class Meta:
        model = Disaster
        attrs = {'class': 'table table-bordered table-striped table-hover'}


class AnimallossTable(tables.Table):
    id = tables.Column(visible=False)
    name = tables.LinkColumn('course_detail', args=[A('pk')])
    class Meta:
        model = Animalloss
        attrs = {'class': 'table table-bordered table-striped table-hover'}


class LocationTable(tables.Table):
    id = tables.Column(visible=False)
    class Meta:
        model = Location
        attrs = {'class': 'table table-bordered table-striped table-hover'}

class HumanlossTable(tables.Table):
    id = tables.Column(visible=False)
    class Meta:
        model = Humanloss
        attrs = {'class': 'table table-bordered table-striped table-hover'}

class DisastertypeTable(tables.Table):
    id = tables.Column(visible=False)
    class Meta:
        model = Disastertype
        attrs = {'class': 'table table-bordered table-striped table-hover'}

class DisastergroupTable(tables.Table):
    id = tables.Column(visible=False)
    class Meta:
        model = Disastergroup
        attrs = {'class': 'table table-bordered table-striped table-hover'}

class PropertylossTable(tables.Table):
    id = tables.Column(visible=False)
    class Meta:
        model = Propertyloss
        attrs = {'class': 'table table-bordered table-striped table-hover'}