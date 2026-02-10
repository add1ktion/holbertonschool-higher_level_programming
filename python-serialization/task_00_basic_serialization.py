"""Module pour sérialisation/désérialisation JSON de dictionnaires."""

import json


def serialize_and_save_to_file(data, filename):
    """Sérialise un dict Python vers fichier JSON.

    Args:
        data (dict): Données à sérialiser
        filename (str): Nom du fichier JSON de sortie
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Charge et désérialise un fichier JSON vers dict Python.

    Args:
        filename (str): Nom du fichier JSON d'entrée

    Returns:
        dict: Données désérialisées
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
