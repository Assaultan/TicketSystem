from django.urls import path,include

from ticket_app.api.views import ListTickets,TicketTitle,TicketDelete,TicketCreate,TicketUpdate


urlpatterns = [
    path('all/',ListTickets.as_view(),name='tickets'),
    path('new/',TicketCreate.as_view(),name='ticket-create'),
    path('',TicketTitle.as_view(),name='ticket-title'),
    path('delete/',TicketDelete.as_view(),name='ticket-delete'),
    path('markAsClosed/',TicketUpdate.as_view(),name='ticket-update'),
]