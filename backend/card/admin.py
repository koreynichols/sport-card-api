from django.contrib import admin
from .models import Card
# Register your models here.

class CardAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Card._meta.fields]

admin.site.register(Card, CardAdmin)