from django.contrib import admin
from .models import Customer, Address, BlogPost, Comment, Student, Course
# Register your models here.

admin.site.register(Customer)
admin.site.register(Address)
admin.site.register(BlogPost)
admin.site.register(Comment)
admin.site.register(Student)
admin.site.register(Course)
