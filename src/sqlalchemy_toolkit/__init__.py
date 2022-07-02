"""sqlalchemy-toolkit."""

from pathlib import Path
import json

# include meta:
meta_file_name = 'meta.json'
dir_path = Path(__file__).resolve().parent
meta_path = dir_path.joinpath(meta_file_name)


def _set_meta(path):
    attrs = list()

    try:
        with open(path) as file:
            meta_dict = json.load(file)
        del file
    except FileNotFoundError:
        meta_dict = dict()

    for attr, value in meta_dict.items():
        globals()[attr] = value
        attrs.append(attr)

    return attrs


__all__ = [*_set_meta(path=meta_path)]

del (Path, json, meta_file_name, dir_path, meta_path, _set_meta)
