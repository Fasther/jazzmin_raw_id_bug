from django.contrib import admin
from django.contrib.admin import ModelAdmin, TabularInline, register

from testj.models import Company, Worker


class WorkerInline(TabularInline):
    raw_id_fields = ("supervisor", )
    model = Worker
    extra = 0


@register(Company)
class CompanyAdmin(ModelAdmin):
    inlines = (WorkerInline, )


@register(Worker)
class WorkerAdmin(ModelAdmin):
    pass
