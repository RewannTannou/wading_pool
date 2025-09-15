import os  # Module pour interagir avec le système de fichiers


def list_files_walk(start_path="."):
    # Parcourt récursivement tous les dossiers et fichiers à partir de start_path
    for root, dirs, files in os.walk(start_path):
        for file in files:
            # Affiche le chemin complet du fichier
            print(os.path.join(root, file))


# Dossier de départ (ici le dossier courant)
directory_path = "./"

# Appel de la fonction
list_files_walk(directory_path)
