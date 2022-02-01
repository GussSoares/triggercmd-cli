import json

from typing import List, Union
from pathlib import Path


class JsonFile:
    @staticmethod
    def load(path: Union[Path, str]) -> List[dict]:
        with open(path, encoding="utf-8") as json_file:
            return json.load(json_file)

    @staticmethod
    def update(path: Union[Path, str], data: List[dict]):
        with open(path, "w+", encoding="utf-8") as json_file:
            json_file.write(
                json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False)
            )