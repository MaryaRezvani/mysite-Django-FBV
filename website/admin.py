from django.contrib import admin
from website.models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    #fields =('title',)
    list_display =('name','email','created_date')
    list_filter=('email',)
    #ordering=['-created_date']
    search_fields = ['message','subject']

# Register your models here.
# admin.site.register(Contact)