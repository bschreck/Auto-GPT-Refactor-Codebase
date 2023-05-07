import os
from typing import Any, Dict, List, Optional, Tuple, TypeVar, TypedDict


def gen_tree(codebase_root: str, indent_depth=0):
    """return an ascii representation of the directory tree at codebase_root/"""
    indent = " " * 4 * (indent_depth)
    tree = "{}{}".format(indent, os.path.basename(codebase_root))
    if not os.path.isdir(codebase_root):
        return tree + "\n"
    tree += "/\n"
    for f in os.listdir(codebase_root):
        full_path = os.path.join(codebase_root, f)
        tree += gen_tree(full_path, indent_depth=indent_depth + 1)
    return tree


def list_dirs(dirs: List[str]):
    repr = ""
    for d in dirs:
        fnames = os.listdir(d)
        ftypes = ["file" if os.path.isfile(os.path.join(d, f)) else "dir" for f in fnames]
        repr += ", ".join(["{}[{}]".format(d, ftype) for d, ftype in zip(fnames, ftypes)])
        repr += "\n"
    return repr


def read_files(filepaths: List[str]):
    return "\n\n--------\n\n".join([read_file(filepath) for filepath in filepaths])


def read_file(filepath: str):
    with open(filepath, "r") as f:
        return f"# {filepath}\n{f.read()}"
