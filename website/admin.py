from django.contrib import admin
from website.models import Contact,Newsletter

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    
    #fields =('title',)
    list_display =('name','email','created_date')
    list_filter=('email',)
    #ordering=['-created_date']
    search_fields = ['message','name']

# Register your models here.
#admin.site.register(Contact,ContactAdmin)
admin.site.register(Newsletter)

