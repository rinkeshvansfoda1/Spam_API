from django.contrib import admin
from .models import Contact

# Register your models here.

# after creating the Table called Contact we have to register here usign admin
admin.site.register(Contact)

# here built-in database is used i.e., SQLite3
# and creating superuser to make some modification at the server side