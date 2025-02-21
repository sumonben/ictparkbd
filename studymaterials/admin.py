from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Lecture,Subject,Chapter
# Register your models here.
@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    list_display=['topic_id','topic_name','file','image','author']
    
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display=['subject_name', 'chapter_number']


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display=['chapter_id', 'chapter_name','subject']