# TicketSystem
Feature Building

Install requirements.txt
> pip -r requirements.txt

create a mongodb database on your machine
named: >TicketingSystem

Run 
>python manage.py makemigrations
>python manage.py migrate

endpoints

to createuser
/users/new/

to create ticket(admin)
/tickets/new/

queries with params in urls
○ /tickets/all will return all tickets
○ /tickets/?status=open/close returns tickets according to status
○ /tickets/?title= searches for the particular title
○ /tickets/?priority=low/medium/high returns ticket according to priority

A Ticket closing endpoint (/tickets/markAsClosed), has to be a POST request, and
accepts ticketID as body param.
○ Auth Token of the user assigned to the ticket can only close the request or
the admin, any other token should return unauthorised
○ Ticket cannot be closed if another higher priority ticket has been assigned
to the same user, returning error ‘A higher priority task remains to be closed’
and also returns all tasks of higher priority

A Ticket deletion endpoint (/tickets/delete), has to be a POST request, and accepts
ticketID as body param. (Only Admin can delete tickets)


