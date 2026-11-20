from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Tache
from .forms import TacheForm


def liste_taches(request):
    """Affiche les tâches avec les filtres commun et spécifique au groupe 5."""
    taches = Tache.objects.all().order_by("-date_creation")
    statut = request.GET.get("statut", "")
    priorite = request.GET.get("priorite", "")

    statuts_valides = {code for code, _ in Tache.STATUTS}
    if statut in statuts_valides:
        taches = taches.filter(statut=statut)
    else:
        statut = ""

    # Fonctionnalité propre au Groupe 5 : afficher les tâches de priorité 1.
    if priorite == "1":
        taches = taches.filter(priorite=1)
    else:
        priorite = ""

    return render(request, "taches/liste.html", {
        "taches": taches,
        "statut_selectionne": statut,
        "priorite_selectionnee": priorite,
        "statuts": Tache.STATUTS,
    })


def creer_tache(request):
    form = TacheForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("liste_taches")
    return render(request, "taches/form.html", {"form": form, "titre": "Nouvelle tâche"})


def modifier_tache(request, pk):
    tache = get_object_or_404(Tache, pk=pk)
    form = TacheForm(request.POST or None, instance=tache)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("liste_taches")
    return render(request, "taches/form.html", {"form": form, "titre": "Modifier la tâche"})


@require_POST
def supprimer_tache(request, pk):
    tache = get_object_or_404(Tache, pk=pk)
    tache.delete()
    return redirect("liste_taches")
