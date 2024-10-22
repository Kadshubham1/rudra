from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'email', 'phone', 'gender', 'date', 'department')
    list_filter = ('gender', 'department', 'date')
    search_fields = ('first_name', 'email', 'phone')
    date_hierarchy = 'date'
    ordering = ('-date', 'first_name')

    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name', 'email', 'phone', 'gender')
        }),
        ('Appointment Details', {
            'fields': ('date', 'department', 'comments')
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return ('date',)
        return self.readonly_fields