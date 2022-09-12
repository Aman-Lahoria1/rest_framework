from django.contrib import admin
from companyre.models import CompanyRecord

# Register your models here.
admin.site.register(CompanyRecord)
class CompanyAdmin(admin.ModelAdmin):
    list_display=['company_name','email_id','company_code','strength']
