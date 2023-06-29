#   #############################  CREACIÓN DE EVENTOS #########################
# Se define un formulario (EventForm) basado en un modelo (Event) utilizando ModelForm de Django.
# Se agregaron widgets para formatear los campos de fecha y hora para que se muestren en el formulario html
# Especificado input_formats para analizar la entrada local de fecha y hora de HTML5 en campos de fecha y hora

# se utiliza la clase DateInput de Django para especificar los widgets de entrada de fecha y hora
from cal.models import Event
from django.forms import ModelForm, DateInput


class EventForm(ModelForm):
    class Meta:
        model = Event
        # datetime-local is a HTML5 input type, format to make date time show on fields
        widgets = {
            'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'end_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
        }
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        # input_formats to parse HTML5 datetime-local input to datetime field
        self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
        self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)
