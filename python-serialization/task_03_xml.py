#!/usr/bin/env python3
"""
Serialize and deserialize dictionaries to/from XML.
"""
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary to XML file.

    Args:
        dictionary (dict): Dictionary to serialize.
        filename (str): XML filename.

    Returns:
        bool: True on success, False on error.
    """
    try:
        root = ET.Element("data")

        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)

        tree = ET.ElementTree(root)
        ET.indent(tree, space="    ", level=0)
        tree.write(filename, encoding="utf-8", xml_declaration=True)

        return True
    except Exception:
        return False


def deserialize_from_xml(filename):
    """
    Deserializes XML file to Python dictionary.

    Args:
        filename (str): XML filename.

    Returns:
        dict: Dictionary from XML, or empty dict on error.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        data = {}
        for child in root:
            data[child.tag] = child.text

        return data
    except Exception:
        return {}
