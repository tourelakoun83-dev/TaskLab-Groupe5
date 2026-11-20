# TaskLab TWIN2 — Groupe 5

## Présentation du projet

TaskLab est une application pédagogique de gestion des tâches développée avec le framework Django dans le cadre du TP de Génie Logiciel TWIN2.

Le projet permet de créer, consulter, modifier, supprimer et filtrer des tâches.

Cette version comprend les fonctionnalités communes du TP ainsi que la variante demandée au Groupe 5.

## Fonctionnalités

- Afficher la liste des tâches.
- Créer une nouvelle tâche.
- Modifier une tâche existante.
- Supprimer une tâche.
- Vérifier les données saisies dans les formulaires.
- Filtrer les tâches selon leur statut : À faire, En cours et Terminée.
- Afficher uniquement les tâches de priorité 1 (variante Groupe 5).
- Combiner le filtre par statut et celui de priorité 1.
- Exécuter des tests automatisés.

## Technologies utilisées

- Python
- Django
- SQLite
- HTML et CSS
- Git et GitHub

## Prérequis

- Python 3.11 ou plus récent.
- Git.
- Visual Studio Code (recommandé).
- Un navigateur web.

## Installation sous Windows

### 1. Récupérer le projet

Cloner le dépôt GitHub :

```bash
git clone https://github.com/tourelakoun83-dev/TaskLab-Groupe5.git
```

Entrer dans le dossier du projet :

```bash
cd TaskLab-Groupe5
```

### 2. Créer l'environnement virtuel

```bash
py -m venv .venv
```

Activer l'environnement :

```powershell
.venv\Scripts\Activate.ps1
```

Si PowerShell bloque l'activation, exécuter :

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Puis recommencer l'activation.

### 3. Installer les dépendances

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Préparer la base de données

```bash
python manage.py migrate
```

### 5. Lancer les tests

```bash
python manage.py test
```

Les tests doivent se terminer sans échec.

### 6. Démarrer l'application

```bash
python manage.py runserver
```

Ouvrir ensuite cette adresse dans le navigateur :

http://127.0.0.1:8000/

## Vérification des fonctionnalités

Pour vérifier le filtre de priorité 1 :

1. Ajouter une tâche avec une priorité de 1.
2. Ajouter une autre tâche avec une priorité de 2.
3. Retourner à la liste des tâches.
4. Cliquer sur le lien permettant d'afficher uniquement les tâches de priorité 1.
5. Vérifier que seules les tâches concernées apparaissent.

Pour vérifier le filtre par statut :

1. Sélectionner un statut.
2. Cliquer sur Appliquer.
3. Vérifier que seules les tâches ayant ce statut sont affichées.

Les deux filtres doivent pouvoir être utilisés ensemble.

## Tests automatisés

Les tests sont exécutés avec la commande :

```bash
python manage.py test
```

Ils permettent notamment de vérifier :

- La création d'une tâche.
- L'affichage de la liste.
- La validation des données.
- La création et la suppression par requête POST.
- Le filtre par statut.
- Le filtre de priorité 1.
- La combinaison des filtres.

## Travail en équipe avec Git et GitHub

Chaque membre du groupe doit travailler sur une branche personnelle.

Exemple :

```bash
git switch -c feature/nom-de-la-fonctionnalite
```

Après les modifications :

```bash
git add .
git commit -m "Description des modifications"
git push -u origin feature/nom-de-la-fonctionnalite
```

Une Pull Request doit ensuite être créée sur GitHub pour proposer l'intégration des modifications dans la branche `main`.

Chaque contribution doit faire l'objet d'une relecture.

## Configuration et fichiers à ne pas versionner

Les fichiers suivants ne doivent pas être envoyés sur GitHub :

- `.env` : contient les paramètres et secrets propres à un environnement.
- `.venv/` : contient l'environnement Python local.
- `db.sqlite3` : contient la base de données locale.
- `__pycache__/` : contient des fichiers temporaires Python.

Le fichier `.gitignore` permet d'exclure ces éléments du dépôt.

## Intégration continue

Le projet utilise GitHub Actions pour automatiser les vérifications.

Le workflow se trouve dans :

`.github/workflows/tests.yml`

Il permet notamment d'installer les dépendances, d'appliquer les migrations et d'exécuter les tests automatiquement lors des événements configurés.

Le résultat des exécutions est consultable dans l'onglet **Actions** du dépôt GitHub.

## Versions du projet

- **v1.0.0** : première version stable après validation de l'implémentation, des tests et de la documentation.
- **v1.1.0** : version intégrant les améliorations et corrections de maintenance validées par le groupe.

Les tags seront créés après validation des versions correspondantes.

## Gestion de projet

Le suivi du travail est organisé dans un tableau Trello comprenant trois colonnes :

- À faire.
- En cours.
- Terminé.

Les tâches suivies comprennent notamment l'installation, les fonctionnalités, les tests, la documentation, la maintenance et la livraison.

## Limites du projet

TaskLab est une application pédagogique destinée à un environnement local.

Cette version ne comprend pas de système d'authentification utilisateur ni de configuration de déploiement en production.