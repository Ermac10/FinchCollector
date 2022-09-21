from django.shortcuts import render

class Finch:
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age

finches = [
    Finch('Gref', 'Green Warbler Finch', 'Warble Weeble', 3),
    Finch('Gryfie', 'Grey Warbler Finch', 'Warble warble', 4),
    Finch('Monfie', 'Mongrove Finch', 'Hates Tuesgroves', 10),
    Finch('Smalf', 'Small Tree Finch', 'Hates Big trees', 0),
]
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {'cats': finches})
