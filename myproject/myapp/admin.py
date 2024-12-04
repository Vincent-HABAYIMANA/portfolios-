from django.contrib import admin

# Register your models here.
from .models import Collector ,Supplies,Items,Transactions,Inventory,Account,Payment,Users,Branch

# @admin.register(Collector)
# class CollectorAdmin(admin.ModelAdmin):
#     list_display = ('collectorID', 'UserName', 'Site', 'Inventory')
admin.site.register(Collector)
admin.site.register(Supplies)
admin.site.register(Items)
admin.site.register(Transactions)
admin.site.register(Inventory)
admin.site.register(Account)
admin.site.register(Payment)
admin.site.register(Users)
admin.site.register(Branch)