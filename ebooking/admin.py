from django.contrib import admin
from django.contrib.auth.models import Permission

from ebooking.models import Room, User, Booking

admin.site.register(Permission)

# Register your models here.
class RoomAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'open_time', 'close_time', 'capacity']
    list_per_page = 10
    list_filter = ['name', 'open_time', 'close_time', 'capacity']
    search_fields = ['name']

admin.site.register(Room, RoomAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'password', 'first_name', 'last_name', 'email'] 
    list_per_page = 15

admin.site.register(User, UserAdmin)


class UserAdmin(admin.ModelAdmin):
    list_display = ['room', 'date', 'start_time', 'end_time', 'description', 'status', 'status_remark', 'book_by', 'book_date']
    list_per_page = 15
admin.site.register(Booking)