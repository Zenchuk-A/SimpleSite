from django.contrib import admin

from .models import Student, Teacher


class StudentInline(admin.StackedInline):
    model = Student
    extra = 0

class StudentAdmin(admin.ModelAdmin):

    list_display = (
        'first_name',
        'last_name',
        'birthday',
        'teacher',
    )

    search_fields = (
        'first_name',
        'last_name',
        'birthday',
        'teacher',
    )

    list_display_links = (
        'first_name',
        'last_name',
    )

    class Meta:
        model = Student
        fields = '__all__'

class TeacherAdmin(admin.ModelAdmin):

    inlines = (
        StudentInline,
    )

    list_display = (
        'first_name',
        'last_name',
    )

    class Meta:
        model = Teacher
        fields = '__all__'

admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
