import os
from typing import Generator
from pathlib import Path



def file_reader(file_path: str) -> str:
    with open(file_path) as f:
        content = f.read()
    return content


def directory_reader(dir_path: str) -> Generator[tuple[Path, str]]:
    dir_content = os.listdir(dir_path)
    for each_path in dir_content:
        if each_path.endswith(".txt"):
            each_path = os.path.join(dir_path, each_path)
            content = file_reader(each_path)
            yield Path(each_path), content
        else:
            each_path = os.path.join(dir_path, each_path)
            yield from directory_reader(each_path)

