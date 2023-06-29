from django.shortcuts import render
from django.http import HttpResponse


# creamos la vista index
def index(request):
    return HttpResponse('hello')


# usamos la clase Calendar que creamos en utils.py aqui
import calendar
from datetime import datetime, timedelta
from datetime import date
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.utils.safestring import mark_safe
from django.http import HttpResponseRedirect
from django.urls import reverse
from urllib.parse import urlencode  # eliminar
from django.shortcuts import render, get_object_or_404

# from .models import *
from .models import Event
from .utils import Calendar
from .forms import EventForm


class CalendarView(generic.ListView):
    model = Event
    template_name = 'cal/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('day', None))
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        return context


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()


# Para acceder a otros meses, cuando estamos en el mes actual, calculamos la fecha del mes anterior y el siguiente
# y las pasamos como variables de plantilla calendar.html:
def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = urlencode({'day': f'{prev_month.year}-{prev_month.month}'})
    return month


def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = urlencode({'day': f'{next_month.year}-{next_month.month}'})
    return month


# Creamos la vista eventos que que maneja la creación y edición de eventos.
# event_idrepresenta el id del evento a actualizar. Si existe,
# sabemos que queremos usar ese objeto y si no es así, queremos un nuevo objeto.
def event(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()

    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('cal:calendar'))
    return render(request, 'cal/event.html', {'form': form})
