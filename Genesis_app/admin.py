from django.contrib import admin
from Genesis_app.models import *

# Register your models here.
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('info_type','info') 

admin.site.register(Home)
admin.site.register(About_message)
admin.site.register(Core_value)
admin.site.register(Expertise)
admin.site.register(Testimonial)
admin.site.register(Team)
admin.site.register(Contact_info, ContactInfoAdmin)