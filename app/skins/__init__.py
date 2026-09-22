from __future__ import annotations

import importlib

KNOWN = ("stub", "listguard", "clausewindow", "menumind", "exhibit")


def load_skin(name: str):
    if name not in KNOWN:
        raise KeyError(f"unknown skin {name}")
    return importlib.import_module(f"skins.{name}")
