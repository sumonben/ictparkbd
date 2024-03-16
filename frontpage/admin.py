from django.contrib import admin
from .models import Carosel
# Register your models here.
@admin.register(Carosel)
class CaroselAdmin(admin.ModelAdmin):
    list_display=['cid', 'cname','ctext','cimage']