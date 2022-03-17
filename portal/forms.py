from django import forms
from .models import Disaster, Location, Propertyloss, Humanloss, Disastertype, Animalloss,Disastergroup

class DisasterForm(forms.ModelForm):
    class Meta:
        model=Disaster
        fields=['id','date','type','source','animallossid','humanlossid','propertylossid']

class LocationForm(forms.ModelForm):
    class Meta:
        model=Location
        fields=('id','tole','municipiality','district')

class PropertlossForm(forms.ModelForm):
    class Meta:
        model=Propertyloss
        fields=('id','fully_damaged_building','partially_damaged_building','estimated_loss')

class HumanLossForm(forms.ModelForm):
    class Meta:
        model = Humanloss
        fields=('id','male_death','female_death','injured','affected_family','dispalced_male','dispalced_female')

class DisasterTypeForm(forms.ModelForm):
    class Meta:
        model = Disastertype
        fields = ('type','category')

class AnimallossForm(forms.ModelForm):
    class Meta:
        model=Animalloss()
        fields=('id','animal_killed','habitat_loss')

class DisastergroupForm(forms.ModelForm):
    class Meta:
        model=Disastergroup()
        fields=('category','disaster_group')