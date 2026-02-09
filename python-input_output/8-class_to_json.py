#!/usr/bin/python3
import json


def class_to_json(obj):
    """Returns dict description with simple
    data structure for JSON serialization."""
    return obj.__dict__
