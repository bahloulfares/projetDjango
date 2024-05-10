from django.shortcuts import render, redirect,get_object_or_404
from .models import Tache
from .forms import TacheForm

def liste_taches(request):
    taches = Tache.objects.all()
    return render(request, 'liste_taches.html', {'taches': taches})

def ajouter_tache(request):
    if request.method == 'POST':
        form = TacheForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_taches')
    else:
        form = TacheForm(initial={'termine': True})  # Pré-cocher la case à cocher (terminée)
    return render(request, 'ajouter_tache.html', {'form': form})

def marquer_termine(request, tache_id):
    tache = get_object_or_404(Tache, id=tache_id)
    tache.termine = True
    tache.save()
    return redirect('liste_taches')

def supprimer_tache(request, tache_id):
    tache = get_object_or_404(Tache, id=tache_id)
    tache.delete()
    return redirect('liste_taches')