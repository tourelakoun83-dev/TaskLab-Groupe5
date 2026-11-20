# Generated for the TaskLab TWIN2 teaching project.
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="Tache",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("titre", models.CharField(max_length=120)),
                ("description", models.TextField(blank=True)),
                ("statut", models.CharField(choices=[("A_FAIRE", "À faire"), ("EN_COURS", "En cours"), ("TERMINEE", "Terminée")], default="A_FAIRE", max_length=12)),
                ("priorite", models.PositiveSmallIntegerField(default=2)),
                ("date_creation", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
