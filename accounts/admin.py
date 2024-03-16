from django.contrib import admin

from django.contrib import admin
from .models import CustomUser
# Register your models here.
@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display=['email', 'name','phone','session','group']