from django.contrib import admin
from .models import Patient, Fields, Question, Option, Complaint


class ChoiceInLineAdmin(admin.TabularInline):
    model = Option


class FieldsAdmin(admin.ModelAdmin):
    inlines = [ChoiceInLineAdmin]


admin.site.register(Patient)
admin.site.register(Question)
admin.site.register(Complaint)
# admin.site.register(Choice)
admin.site.register(Fields, FieldsAdmin)
