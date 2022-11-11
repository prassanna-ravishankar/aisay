import rootpath
from pathlib import Path


def test_dir():
    return Path(rootpath.detect()) / "tests"