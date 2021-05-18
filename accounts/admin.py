from django.contrib import admin

from .models import Comment ,Profile , Appointment , Category

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name','address','number_phone','doctor' , 'Specialist_doctor')
    list_filter = ('type_doctors'  , 'address' ,'price')
    search_fields = ('name','address')
    # prepopulated_fields = {'slug' : ('name' ,)} To create automatically slug when i create name
admin.site.register(Profile , ProfileAdmin)
admin.site.register(Comment)
admin.site.register(Appointment)
admin.site.register(Category)
