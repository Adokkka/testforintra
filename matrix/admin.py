from django.contrib import admin

# Register your models here.

from .models import *
admin.site.register(Task)
admin.site.register(DataItem)
admin.site.register(Customer)
#admin.site.register(Service)
#admin.site.register(Matrix)
admin.site.register(Expenditure)