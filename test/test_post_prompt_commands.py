import os
from src.auto_gpt_refactor_codebase.refactor_codebase import (
    gen_tree,
    list_dirs,
)


def test_gen_tree_no_codebase_root():
    os.environ["CODEBASE_ROOT"] = ""
    assert gen_tree() == "No codebase root found. Set the CODEBASE_ROOT environment variable."


def test_gen_tree():
    os.environ["CODEBASE_ROOT"] = "test/fake_codebase"
    print(gen_tree())
    assert (
        gen_tree()
        == """fake_codebase/
    fake_codebase.py
    __init__.py
    utils/
        __init__.py
        file_utils.py
"""
    )


def test_list_dirs():
    assert (
        list_dirs(["test/fake_codebase", "test/fake_codebase/utils"])
        == """fake_codebase.py[file], __init__.py[file], utils[dir]
__init__.py[file], file_utils.py[file]
"""
    )
