from django.urls import path
from ticket_app.api.views import ListTickets
urlpatterns = [
    path('all/',ListTickets.as_view(),name='tickets'),
]
