from django.contrib import admin
from .models import User

@admin.register(User)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'password', 'is_admin', 'is_reader',
                  "first_name","last_name", 'is_librarian',"phone_number","age","gender")



