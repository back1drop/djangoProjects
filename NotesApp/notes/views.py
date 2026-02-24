from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import Note
from .forms import NoteForm

# Create your views here.
@login_required
def note_list(request):
    notes=Note.objects.filter(owner=request.user).order_by('-created_at')
    return render(request,'note_list.html',{'notes': notes})

#object level permission(checking both the object exists AND belongs to the current user)
@login_required
def note_detail(request,pk):
    note=get_object_or_404(Note,pk=pk,owner=request.user)
    return render(request,'note_detail.html',{'note':note})

@login_required
def note_create(request):
    if request.method=='POST':
        form=NoteForm(request.POST)
        if form.is_valid():
            note=form.save(commit=False)
            note.owner=request.user
            note.save()
            return redirect('note_list')
    else:
        form=NoteForm()
    return render (request,'note_form.html',{'form':form})