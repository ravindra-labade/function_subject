from django.shortcuts import render, redirect
from .forms import SubjectForm
from .models import Subject



def add_subject(request):
    template_name = 'subj/add.html'
    form = SubjectForm()
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form': form}
    return render(request, template_name, context)


def show_subject(request):
    template_name = 'subj/show.html'
    subjects = Subject.objects.all()
    context = {'subjects': subjects}
    return render(request, template_name, context)


def update_subject(request, pk):
    template_name = 'subj/add.html'
    obj = Subject.objects.get(id=pk)
    form = SubjectForm(instance=obj)
    if request.method == 'POST':
        form = SubjectForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form': form}
    return render(request, template_name, context)



def cancel_subject(request, pk):
    obj = Subject.objects.get(id=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('show_url')
    return render(request, 'subj/confirm.html')