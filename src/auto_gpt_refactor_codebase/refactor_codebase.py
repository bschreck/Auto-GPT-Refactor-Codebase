import os
from typing import Any, Dict, List, Optional, Tuple, TypeVar, TypedDict


def gen_tree():
    """return an ascii representation of the directory tree at CODEBASE_ROOT"""
    root = os.getenv("CODEBASE_ROOT")
    if not root:
        return "No codebase root found. Set the CODEBASE_ROOT environment variable."

    return _gen_tree(root)


def _gen_tree(root: str, indent_depth=0):
    """return an ascii representation of the directory tree at root/"""
    indent = " " * 4 * (indent_depth)
    tree = "{}{}".format(indent, os.path.basename(root))
    if not os.path.isdir(root):
        return tree + "\n"
    tree += "/\n"
    for f in os.listdir(root):
        full_path = os.path.join(root, f)
        tree += _gen_tree(full_path, indent_depth=indent_depth + 1)
    return tree


def list_dirs(dirs: List[str]):
    repr = ""
    for d in dirs:
        fnames = os.listdir(d)
        ftypes = ["file" if os.path.isfile(os.path.join(d, f)) else "dir" for f in fnames]
        repr += ", ".join(["{}[{}]".format(d, ftype) for d, ftype in zip(fnames, ftypes)])
        repr += "\n"
    return repr
