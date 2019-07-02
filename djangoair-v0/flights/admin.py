from django.contrib import admin

from .models import Airport, Flight

# Register your models here.
# admin is an app built-in on djando
# and makes very easy to modify and update data in existing models
# what I am doing here is, making admin able to manipulate Airport and Flight
admin.site.register(Airport)
admin.site.register(Flight)