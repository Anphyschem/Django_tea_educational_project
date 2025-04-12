from django import forms
from .models import Tea
from django.core.validators import MinValueValidator

class Tea_form(forms.ModelForm):
    water_temperature = forms.IntegerField(
        label='Температура воды (°C)',
        validators=[MinValueValidator(20)],
        error_messages={'min_value': 'Температура не может быть меньше 20°C'} 
    )
    spillage_number = forms.IntegerField(
        label='Число проливов',
        validators=[MinValueValidator(1)],
        error_messages={'min_value': 'Число проливов не может быть меньше одного!'}
    )
    class Meta:
        model = Tea
        fields = ['type_of_tea', 'title', 'water_temperature','spillage_number', 'description']
        widgets = {
            'type_of_tea': forms.Select(attrs={'class': 'form-control'}),
        }
    