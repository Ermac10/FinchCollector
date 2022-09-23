from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import FeedingForm

from .models import Finch, Toy

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {'finches': finches})

class ToyIndex(ListView):
    model = Toy

def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    feeding_form = FeedingForm()
    return render(request, 'finches/detail.html', {
        'finch': finch, 'feeding_form' : feeding_form
        })

def add_feeding(request, finch_id):
    form = FeedingForm(request.POST)

    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.finch_id = finch_id
        new_feeding.save()
    return redirect('detail', finch_id=finch_id)

class ToyDetail(DetailView):
    model = Toy

class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'

class ToyCreate(CreateView):
    model = Toy
    fields = '__all__'

class FinchUpdate(UpdateView):
    model = Finch
    fields = ('age', 'breed', 'description')

class ToyUpdate(UpdateView):
    model = Toy
    fields = ('__all__')

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches/'

class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys/'