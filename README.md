# TaskLab TWIN2 — Groupe 5

Application pédagogique de gestion des tâches réalisée avec Django. Cette version contient les fonctionnalités communes demandées dans le TP et la variante du **Groupe 5**.

## Fonctionnalités
- Afficher la liste des tâches, créer, modifier et supprimer une tâche.
- Valider les données du formulaire (priorité comprise entre 1 et 3).
- **Filtre commun :** filtrer la liste par statut (`A_FAIRE`, `EN_COURS`, `TERMINEE`).
- **Variante Groupe 5 :** afficher uniquement les tâches de priorité 1 avec le lien « Afficher uniquement les tâches de priorité 1 » (`?priorite=1`).
- Combiner le filtre par statut et le filtre de priorité 1.
- Tests automatisés couvrant les opérations et les filtres.

## Prérequis
- Python 3.11 ou plus récent
- Git
- Un terminal (PowerShell sous Windows)

## Installation sous Windows (PowerShell)
Ouvrir le dossier du projet dans VS Code, puis ouvrir **Terminal > Nouveau terminal** et exécuter les commandes une par une :

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
python manage.py test
python manage.py runserver
```

Si PowerShell bloque l'activation de l'environnement, exécuter dans le terminal :
`Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`, puis recommencer l'activation.

Ouvrir ensuite http://127.0.0.1:8000/ dans le navigateur.

## Tests
```powershell
python manage.py test
```
Le résultat attendu est `OK` et zéro échec. Les tests vérifient la création du modèle, l'accès à la liste, la validation du formulaire, la création et la suppression par POST, le filtre par statut, le filtre Groupe 5 et leur combinaison.

## Démonstration de la variante Groupe 5
1. Ajouter une tâche avec priorité `1`.
2. Ajouter une autre tâche avec priorité `2`.
3. Revenir à la liste et cliquer sur « Afficher uniquement les tâches de priorité 1 ».
4. Vérifier que seule la tâche de priorité 1 apparaît.
5. Sélectionner un statut puis appliquer le filtre : les deux filtres peuvent être utilisés ensemble.

## Git et GitHub — travail en équipe
Chaque membre doit travailler sur une branche personnelle, par exemple `feature/filtre-priorite-1`, faire des commits explicites, puis ouvrir une Pull Request vers `main`. Faire relire le code par un autre membre avant fusion.

Exemple de commandes :
```bash
git init
git add .
git commit -m "chore: initialiser TaskLab groupe 5"
git branch -M main
git remote add origin URL_DU_DEPOT_GITHUB
git push -u origin main
```

Créer ensuite une branche pour une fonctionnalité :
```bash
git switch -c feature/filtre-priorite-1
git add .
git commit -m "feat: ajouter le filtre des tâches de priorité 1"
git push -u origin feature/filtre-priorite-1
```

Ne jamais versionner `.env`, `.venv` ou `db.sqlite3` : ils contiennent respectivement la configuration locale/secrets, l'environnement Python installé et la base de données locale. Le fichier `.gitignore` les exclut.

## Intégration continue
Le workflow `.github/workflows/tests.yml` installe Python et Django, applique les migrations et exécute les tests à chaque push et Pull Request. Sur GitHub, consulter l'onglet **Actions** et vérifier que l'exécution est verte.

## Versions du TP
- `v1.0.0` : version stable de base après implémentation, tests et documentation.
- `v1.1.0` : ajout des filtres par statut et priorité 1 (variante Groupe 5), avec tests associés.

Ces tags doivent être créés dans le dépôt GitHub sur les commits correspondants après validation du groupe.

## Gestion de projet
Créer un tableau Trello avec les colonnes **À faire**, **En cours** et **Terminé**. Prévoir au moins six cartes/issues avec un responsable : installation, filtre par statut, filtre priorité 1, tests, documentation, revue et livraison.

## Limites
Ce projet est un support de TP local. Il n'inclut pas d'authentification utilisateur ni de configuration de déploiement en production.
