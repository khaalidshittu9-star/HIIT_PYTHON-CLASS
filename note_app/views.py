from django.shortcuts import render, redirect
from .models import Note

# Create your views here.


def note_detail(request, pk):
    try:
        note = Note.objects.get(pk=pk)
    except Note.DoesNotExist:
        return render(request, 'note_app/note_not_found.html')
    return render(request, 'note_app/note_detail.html', {'note': note})
    

def note_list(request) :
    notes = Note.objects.all().order_by('created_at')
    return render(request, 'note_app/note_list.html', {'notes': notes})

def create_note(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        note = Note.objects.create(title=title, content=content)
        return redirect('note_list')
    return render(request, 'note_app/create_note.html')

def edit_note(request, pk):
    try:
         note = Note.objects.get(pk=pk)
    except Note.DoesNotExist:
        return render(request, 'note_app/note_not_found.html')     
    if request.method == 'POST':
        note.title = request.POST.get('title')   
        note.content = request.POST.get('content')
        note.save()
        return redirect('note_list')    
    return render(request, 'note_app/edit_note.html', {'note': note})  

def delete_note(request, pk):
    try:
        note = Note.objects.get(pk=pk)
    except Note.DoesNotExist:
        return render(request, 'note_app/note_not_found.html')
    if request.method in ['POST', 'DELETE']:
        note.delete()
        return redirect('note_list')
    return render(request, 'note_app/note_confirm_delete.html', {'note': note})

# select * ` from note_app_note order by created_at desc;`
    # select * ' from note_app_note order by created_at desc;'
    