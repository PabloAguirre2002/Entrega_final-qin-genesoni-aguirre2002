from os import access
from django.contrib import admin
from apponline.models import Carteras, Camperas, Zapatos, Accesorios, Avatar 

admin.site.register(Carteras)
admin.site.register(Camperas)
admin.site.register(Zapatos)
admin.site.register(Accesorios)
admin.site.register(Avatar) 