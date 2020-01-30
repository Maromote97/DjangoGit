from django.contrib import admin

from django.contrib import admin
from .models import Klient
admin.site.register(Klient)

from .models import Pracownik
admin.site.register(Pracownik)

from .models import Ksiazka
admin.site.register(Ksiazka)

from .models import Wypozyczanie
admin.site.register(Wypozyczanie)