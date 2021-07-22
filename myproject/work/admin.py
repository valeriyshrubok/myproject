from django.contrib import admin

from .models import *

class EmloyeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'position_id', 'chief_id', 'salary_id', 'paid_salary_id')
    list_display_links = ('name', 'chief_id')
    search_fields = ('name', 'position_id')
    list_filter = ('position_id', 'lvl')
    actions = ['delete_total_paid']

    def delete_total_paid(self, request, queryset):
        pass
    delete_total_paid.short_description = " Удалить всю информацию о выплаченной заработной плате"

admin.site.register(Employee, EmloyeeAdmin)
admin.site.register(Position)
admin.site.register(Salary)
admin.site.register(Salary_info)
admin.site.register(Chief)


