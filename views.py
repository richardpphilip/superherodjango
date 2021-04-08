from django.shortcuts import render, redirect, get_object_or_404
from .models import SuperheroList
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


# Create your views here.

def index(request):
    all_superheroes = SuperheroList.objects.all()
    print(all_superheroes)
    context = {
        'all_superheroes': all_superheroes
    }
    return render(request, 'superhero_list/index.html', context)


def detail(request, superhero_id):
    superhero = SuperheroList.objects.get(pk=superhero_id)
    print(superhero)
    pk_context = {
        'superhero': superhero
    }
    return render(request, 'superhero_list/detail.html', pk_context)


def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        primary_ability = request.POST.get('primary_ability')
        secondary_ability = request.POST.get('secondary_ability')
        catchphrase = request.POST.get('catchphrase')
        new_superhero = SuperheroList(name=name, primary_ability=primary_ability, secondary_ability=secondary_ability,
                                      catchphrase=catchphrase)
        new_superhero.save()
        return HttpResponseRedirect(reverse('superhero_list:index'))
    else:
        return render(request, 'superhero_list/create.html')


def delete(request, superhero_id):
    context = {}
    superhero = SuperheroList.objects.get(pk=superhero_id)
    if request.method == 'POST':
        superhero.delete()
        return HttpResponseRedirect(reverse('superhero_list:index'))
    context['superhero'] = superhero
    return render(request, 'superhero_list/delete.html', context)


def update(request, superhero_id):
    if request.method == 'POST':
        superhero = SuperheroList.objects.get(pk=superhero_id)
        superhero.name = request.POST.get('name')
        superhero.primary_ability = request.POST.get('primary_ability')
        superhero.secondary_ability = request.POST.get('secondary_ability')
        superhero.catchphrase = request.POST.get('catchphrase')
        superhero.save()
        return HttpResponseRedirect(reverse('superhero_list:index'))
    else:
        return render(request, 'superhero_list/update.html')