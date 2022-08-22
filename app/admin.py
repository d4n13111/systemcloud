from django.contrib import admin
from  embed_video.admin  import  AdminVideoMixin
from .models import Person, Contact, Slider, Service, Portfolio

class FolioAdmin(AdminVideoMixin, admin.ModelAdmin):
	pass

admin.site.register(Person)
admin.site.register(Contact)
admin.site.register(Slider)
admin.site.register(Service)
admin.site.register(Portfolio, FolioAdmin)