from django.contrib import admin
from .models import Disaster, Location, Propertyloss, Humanloss, Disastertype, Animalloss,Disastergroup

# Register your models here.
admin.site.register(Disaster),
admin.site.register(Location),
admin.site.register(Propertyloss),
admin.site.register(Humanloss),
admin.site.register(Disastertype),
admin.site.register(Animalloss),
admin.site.register(Disastergroup),