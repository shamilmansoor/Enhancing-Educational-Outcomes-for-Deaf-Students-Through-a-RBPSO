from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Student, Teacher
from .utils import predict_marks
from .forms import StudentForm, TeacherForm

def home(request):
    student = None
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        try:
            student = Student.objects.get(student_id=student_id)
        except Student.DoesNotExist:
            messages.error(request, 'Student not found')
    return render(request, 'core/home.html', {'student': student})

@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request, 'core/student_list.html', {'students': students})

@login_required
def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'core/edit_student.html', {'form': form, 'student': student})

@login_required
def new_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.predicted_marks = 0
            student.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'core/new_student.html', {'form': form})

@login_required
def predict_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    predicted_marks = predict_marks(student)
    student.predicted_marks = predicted_marks
    student.save()
    messages.success(request, f'Predicted marks: {predicted_marks:.2f}')
    return redirect('student_list')

@login_required
def predict_all(request):
    students = Student.objects.all()
    for student in students:
        predicted_marks = predict_marks(student)
        student.predicted_marks = predicted_marks
        student.save()
    messages.success(request, 'Predicted marks for all students successfully!')
    return redirect('student_list')

def teacher_login(request):
    if request.user.is_authenticated:
        return redirect('student_list')
        
    if request.method == 'POST':
        name = request.POST.get('username')  # We'll use the name field as username
        password = request.POST.get('password')
        
        if not name or not password:
            messages.error(request, 'Please enter both name and password')
            return render(request, 'core/login.html')
            
        try:
            teacher = Teacher.objects.get(name=name, password=password)
            # Create or get a User instance for this teacher
            user, created = User.objects.get_or_create(
                username=teacher.name,
                defaults={'is_staff': True}
            )
            if created:
                user.set_password(password)
                user.save()
            
            login(request, user)
            messages.success(request, f'Welcome back, {teacher.name}!')
            return redirect('student_list')
        except Teacher.DoesNotExist:
            messages.error(request, 'Invalid name or password')
            
    return render(request, 'core/login.html')
