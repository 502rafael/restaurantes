from django.forms import ModelForm, fields
from .models import Alimentos
class AlimentosForm(ModelForm):
    class Meta :
        model = Alimentos
        fields = '__all__'
