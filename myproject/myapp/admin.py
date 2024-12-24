from django.contrib import admin

# Register your models here.
from .models import Collector1,WasteSubmission,PaymentInfo,Users,Branch,Category,RecyclingInfo,Feature,Message,Step,RecyclingInfo1,PaymentRequest,CardDetail,Payment1

# @admin.register(Collector)
# class CollectorAdmin(admin.ModelAdmin):
#     list_display = ('collectorID', 'UserName', 'Site', 'Inventory')
admin.site.register(Collector1)
admin.site.register(WasteSubmission)
admin.site.register(PaymentInfo)
admin.site.register(Users)
admin.site.register(Branch)
admin.site.register(Category)
admin.site.register(RecyclingInfo)
admin.site.register(Feature)
admin.site.register(Step)
admin.site.register(Message)
admin.site.register(PaymentRequest)
admin.site.register(RecyclingInfo1)
admin.site.register(CardDetail)
@admin.register(Payment1)
class Payment1Admin(admin.ModelAdmin):
    list_display = ('name_requester', 'item_name', 'amount', 'created_at')
    list_filter = ('created_at',)
    