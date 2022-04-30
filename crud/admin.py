from django.contrib import admin

# Register your models here.
from .models import Crud
@admin.register(Crud)
class CrudAdmin(admin.ModelAdmin):
    list_display = ('book_id','name','author','genre','edition','author')
