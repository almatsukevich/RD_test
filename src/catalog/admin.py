from django.contrib import admin
from . import models
from django.utils.html import format_html

@admin.action(description='Удалить данные о выплаченной зарплате')
def delete_payd_salary(modeladmin, request, queryset):
    queryset.update(payd_salary=0)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'chief_link', 'salary', 'payd_salary']
    list_filter = ['position', 'level']
    actions = [delete_payd_salary]

    def chief_link(self, obj):
        return format_html(f"<a href='/admin/catalog/employee/{obj.chief}'>{obj.chief}</a>")
    chief_link.allow_tags=True



class LevelAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']

class ChiefAdmin(admin.ModelAdmin):
    list_display = ['pk', 'chief']

class PositionAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']

admin.site.register(models.Employee, EmployeeAdmin)
admin.site.register(models.Level, LevelAdmin)
admin.site.register(models.Chief, ChiefAdmin)
admin.site.register(models.Position, PositionAdmin)