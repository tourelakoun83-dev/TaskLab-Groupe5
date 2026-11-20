from django.test import TestCase
from django.urls import reverse
from .models import Tache
from .forms import TacheForm


class TacheTests(TestCase):
    def test_creation_modele(self):
        tache = Tache.objects.create(titre="Réviser Django")
        self.assertEqual(str(tache), "Réviser Django")

    def test_liste_accessible(self):
        response = self.client.get(reverse("liste_taches"))
        self.assertEqual(response.status_code, 200)

    def test_formulaire_accepte_priorite_valide(self):
        form = TacheForm(data={"titre": "Réviser", "description": "", "statut": "A_FAIRE", "priorite": 1})
        self.assertTrue(form.is_valid())

    def test_formulaire_refuse_priorite_invalide(self):
        form = TacheForm(data={"titre": "Réviser", "description": "", "statut": "A_FAIRE", "priorite": 4})
        self.assertFalse(form.is_valid())
        self.assertIn("priorite", form.errors)

    def test_creation_via_post(self):
        response = self.client.post(reverse("creer_tache"), {
            "titre": "Préparer le TP", "description": "Groupe 5",
            "statut": "A_FAIRE", "priorite": 1,
        })
        self.assertRedirects(response, reverse("liste_taches"))
        self.assertTrue(Tache.objects.filter(titre="Préparer le TP", priorite=1).exists())

    def test_suppression_via_post(self):
        tache = Tache.objects.create(titre="À supprimer")
        response = self.client.post(reverse("supprimer_tache", args=[tache.pk]))
        self.assertRedirects(response, reverse("liste_taches"))
        self.assertFalse(Tache.objects.filter(pk=tache.pk).exists())

    def test_suppression_refusee_en_get(self):
        tache = Tache.objects.create(titre="À conserver")
        response = self.client.get(reverse("supprimer_tache", args=[tache.pk]))
        self.assertEqual(response.status_code, 405)
        self.assertTrue(Tache.objects.filter(pk=tache.pk).exists())

    def test_filtre_par_statut(self):
        Tache.objects.create(titre="En cours", statut="EN_COURS", priorite=2)
        Tache.objects.create(titre="TACHE_TERMINEE_TEST", statut="TERMINEE", priorite=1)
        response = self.client.get(reverse("liste_taches"), {"statut": "EN_COURS"})
        self.assertContains(response, "En cours")
        self.assertNotContains(response, "TACHE_TERMINEE_TEST")

    def test_groupe5_filtre_priorite_1(self):
        Tache.objects.create(titre="Prioritaire", priorite=1)
        Tache.objects.create(titre="Normale", priorite=2)
        response = self.client.get(reverse("liste_taches"), {"priorite": "1"})
        self.assertContains(response, "Prioritaire")
        self.assertNotContains(response, "Normale")

    def test_filtres_statut_et_priorite_combines(self):
        Tache.objects.create(titre="Correspond", statut="EN_COURS", priorite=1)
        Tache.objects.create(titre="Mauvaise priorité", statut="EN_COURS", priorite=2)
        Tache.objects.create(titre="Mauvais statut", statut="A_FAIRE", priorite=1)
        response = self.client.get(reverse("liste_taches"), {"statut": "EN_COURS", "priorite": "1"})
        self.assertContains(response, "Correspond")
        self.assertNotContains(response, "Mauvaise priorité")
        self.assertNotContains(response, "Mauvais statut")
