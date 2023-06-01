from django.urls import path
from .views import GoogleCalendarRedirectView

Urlplt = [
    path('rest/v1/calendar/init/', googleclnvw.as_view(), name='calendar-init'),
    path('rest/v1/calendar/redirect/', gldclnrrdrctvw.as_view(), name='calendar-redirect'),
    
]