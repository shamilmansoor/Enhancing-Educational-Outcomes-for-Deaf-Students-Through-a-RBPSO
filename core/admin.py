from django.contrib import admin
from .models import Student, Teacher

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'student_id', 'age', 'sex', 'address', 'hearing_loss', 'predicted_marks')
    list_filter = ('sex', 'address', 'hearing_loss', 'school_support', 'paid_classes', 'nursery_attendance', 'internet_access', 'extracurricular')
    search_fields = ('name', 'student_id')
    ordering = ('name',)
