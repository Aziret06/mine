from django.contrib import admin

from . import models


@admin.register(models.Tours)
class ToursAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)


@admin.register(models.EasyGO)
class EasyGoAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)
        
        
@admin.register(models.VisaGo)
class VisaGosAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)
    

@admin.register(models.Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)


@admin.register(models.Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)
    