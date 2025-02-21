from django.contrib import admin
from .models import Carosel,News
# Register your models here.
@admin.register(Carosel)
class CaroselAdmin(admin.ModelAdmin):
    list_display=['cid', 'cname','ctext','cimage']

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display=[ 'title','body','image']