from django.contrib import admin

from .models import Employee, Chief, Paid_salary

class EmloyeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'position', 'chief', 'salary', 'paid_salary')
    list_display_links = ('id', 'chief')
    search_fields = ('name', 'position')
    list_filter = ('position', 'lvl')

admin.site.register(Employee, EmloyeeAdmin)
admin.site.register(Chief)
admin.site.register(Paid_salary)