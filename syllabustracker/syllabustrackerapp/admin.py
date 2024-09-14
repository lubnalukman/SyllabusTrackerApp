#from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

# Register your models here.
class MasterAdmin(admin.ModelAdmin):

    # in order to exclude the field 'created_user' from the form
    exclude = ['created_user']

    list_per_page = 10
    def has_delete_permission(self, request, obj=None):
        # Disable delete
        return False

    # To order Active field last in all forms
    def get_fields(self, request, obj=None, **kwargs):
        fields = super().get_fields(request, obj, **kwargs)
        fields.remove('isactive')
        fields.append('isactive')  # can also use insert
        return fields

  # To save the logged in user id to the table when a record is added.
    # https://stackoverflow.com/questions/6760602/how-can-i-get-current-logged-user-id-in-django-admin-panel
    def save_model(self, request, obj, form, change):
        obj.created_user = request.user
        #print(eval(self._class.name_))
        super().save_model(request, obj, form, change)

class TransactionAdmin(admin.ModelAdmin):

    # in order to exclude the field 'created_user' from the form
    exclude = ['created_user']
    
    def has_delete_permission(self, request, obj=None):
        # Disable delete
        return False

class CourseAdmin(MasterAdmin):
    list_display = ['course', 'isactive']

class DayAdmin(MasterAdmin):
    list_display = ['day', 'isactive']

class SyllabusAdmin(MasterAdmin):
    list_display = ['syllabus', 'isactive']

class CourseSyllabusAdmin(TransactionAdmin):
    list_display = ['course','day','get_syllabus']
    filter_horizontal=['syllabus']

    def get_syllabus(self, obj):
        return ", ".join([p.syllabus for p in obj.syllabus.all()])
        

    get_syllabus.allow_tags = True
    get_syllabus.short_description = "Syllabus"

admin.site.register(Course,CourseAdmin)
admin.site.register(Day,DayAdmin)
admin.site.register(Syllabus,SyllabusAdmin)
admin.site.register(CourseSyllabus,CourseSyllabusAdmin)