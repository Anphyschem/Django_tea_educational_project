from calendar import c
from django.db import models
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator

class Tea(models.Model):
    CATEGORY_CHOICES = [
    # (значение для БД,   отображаемое имя)
    ("Green",             "Зелёные"),
    ("White",             "Белые"), 
    ("Oolong",            "Улуны"),
    ("Red",               "Красные"),
    ("Black tea and puers", "Черные и пуэры"),
    ("Herbal tea",        "Не чай"),
    ("Other",             "Другое")
    ]
    type_of_tea = models.CharField('Тип чая', max_length=20, choices=CATEGORY_CHOICES, default="Other")
    title = models.CharField('Название чая', max_length=100)
    water_temperature = models.IntegerField('Температура заваривания (°C)', default=100, validators=[
            MinValueValidator(20),
            MaxValueValidator(100) 
        ])
    spillage_number = models.IntegerField('Число проливов', default=5, validators=[
            MinValueValidator(1),
            MaxValueValidator(25) 
        ])
    description = models.TextField('Описание', max_length=1000)

    def __str__(self):
        return self.title
