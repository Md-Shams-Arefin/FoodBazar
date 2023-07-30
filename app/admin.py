from django.contrib import admin

from .models import *


class Booking(admin.ModelAdmin):
    list_display = ("name",  "email", "date", "people", "phone")


class Messaging(admin.ModelAdmin):
    list_display = ("name",  "email", "subject", "message")


admin.site.register(Book_a_table, Booking)
admin.site.register(Message, Messaging)
