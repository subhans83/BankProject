from django.contrib import admin

# Register your models here.
from bankingapp.models import Branch, District, Register

admin.site.register(Branch)
admin.site.register(District)
admin.site.register(Register)