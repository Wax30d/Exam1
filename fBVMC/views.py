from django.shortcuts import render
from .models import Customer, Address, BlogPost, Comment, Student, Course


# Create your views here.
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customers.html', {'customer_list': customers})


def customer_detail(request, pk):
    customer = Customer.objects.get(pk=pk)
    return render(request, 'customer_detail.html', {'customer': customer})


def address_list(request):
    addressess = Address.objects.all()
    return render(request, 'addressess.html', {'address_list': addressess})


def address_detail(request, pk):
    address = Address.objects.get(pk=pk)
    return render(request, 'address_detail.html', {'address': address})


def blog_list(request):
    blogs = BlogPost.objects.all()
    return render(request, 'blogs.html', {'blog_list': blogs})


def blog_detail(request, pk):
    blog = BlogPost.objects.get(pk=pk)
    return render(request, 'blog_detail.html', {'blog': blog})


def comment_list(request):
    comments = Comment.objects.all()
    return render(request, 'comments.html', {'comment_list': comments})


def comment_detail(request, pk):
    comment = Comment.objects.get(pk=pk)
    return render(request, 'comment_detail.html', {'comment': comment})


def student_list(request):
    students = Student.objects.all()
    return render(request, 'students.html', {'student_list': students})


def student_detail(request, pk):
    student = Student.objects.get(pk=pk)
    return render(request, 'student_detail.html', {'student': student})


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses.html', {'course_list': courses})


def course_detail(request, pk):
    course = Course.objects.get(pk=pk)
    return render(request, 'course_detail.html', {'course': course})
