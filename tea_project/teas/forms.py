from wsgiref.validate import validator
from django import forms
from .models import Tea
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator

class Tea_form(forms.ModelForm):
    water_temperature = forms.IntegerField(
        label='Температура воды (°C)',
        validators=[MinValueValidator(20), MaxValueValidator(100)],
        error_messages={'min_value': 'Температура не может быть меньше 20°C', 'max_value': 'Температура не может быть больше 100°C'} 
    )
    spillage_number = forms.IntegerField(
        label='Число проливов',
        validators=[MinValueValidator(1), MaxValueValidator(25)],
        error_messages={'min_value': 'Число проливов не может быть меньше одного!', 'max_value': 'Слишком много проливов, это уже просто кипяток!'}
    )
    class Meta:
        model = Tea
        fields = ['type_of_tea', 'title', 'water_temperature','spillage_number', 'description']
        widgets = {
            'type_of_tea': forms.Select(attrs={'class': 'form-control'}),
        }
    