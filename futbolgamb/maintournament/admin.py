from django.contrib import admin
from .models import Principal

# Register your models here.

class PrincipalAdmin(admin.ModelAdmin):	
	list_display = ('Namelg_principal', 'federationorg_principal')

admin.site.register(Principal,PrincipalAdmin)