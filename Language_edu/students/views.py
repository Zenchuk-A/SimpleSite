from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator

from .forms import StudentForm
from .models import Student


STUDENTS_PER_PAGE = 7


def students_list(request):
    students = Student.objects.order_by('id')
    paginator = Paginator(students, STUDENTS_PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'students/students_list.html', context)


def student(request, pk=None):
    if pk is not None:
        isinstance = get_object_or_404(Student, pk=pk)
    else:
        isinstance = None

    form = StudentForm(
        request.POST or None, files=request.FILES or None, instance=isinstance
    )
    context = {'form': form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return render(request, 'students/student.html', context)


def student_delete(request, pk):
    isinstance = get_object_or_404(Student, pk=pk)
    form = StudentForm(instance=isinstance)
    context = {'form': form}
    if request.method == 'POST':
        isinstance.delete()
        return redirect('students:students_list')
    return render(request, 'students/student.html', context)
