from django.contrib import admin
from .models import ChaiVerity, ChaiReview, Store, ChaiCertificate

# Register your models here.
class ChaiReviewInLine(admin.TabularInline): 
    model = ChaiReview
    extra = 2

class ChaiVerityAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_added')
    inlines = [ChaiReviewInLine]

class StoreAdmin(admin.ModelAdmin): 
    list_display = ('name', 'location')
    filter_horizontal = ('chai_verities',)

class ChaiCertificateAdmin(admin.ModelAdmin): 
    list_display = ('chai', 'certificate_number')


admin.site.register(ChaiVerity, ChaiVerityAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(ChaiCertificate, ChaiCertificateAdmin)