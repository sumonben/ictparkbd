from django.contrib import admin
from .models import Payment
# Register your models here.
@admin.register(Payment)
class CaroselAdmin(admin.ModelAdmin):
    list_display=['email', 'user_id','phone','month','start_date','end_date']