from .models import PhaseA
from django.contrib import admin

# Register your models here.

class PhaseAAdmin(admin.ModelAdmin):	
	list_display = ('group_fasea',)

admin.site.register(PhaseA,PhaseAAdmin)