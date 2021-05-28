from django.forms import ModelForm, TextInput
from . models import Cities


class CityForm(ModelForm):
    class Meta:
        model = Cities 
        fields = ['visited']
        widgets = {'name' : TextInput(attrs={'class' : 'input','placeholder' : 'Add Place'})}
        
