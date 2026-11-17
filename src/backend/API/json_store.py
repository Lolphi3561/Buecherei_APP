import json
from pathlib import Path
from threading import Lock

class JsonStore:
    def __init__(self, path: str = "books.json"):
        self.path = Path(path)
        self.lock = Lock()
        if not self.path.exists():
            self.path.write_text("[]", encoding="utf-8")

    def load(self) -> list[dict]:
        with self.lock:
            return json.loads(self.path.read_text(encoding="utf-8"))

    def save(self, data: list[dict]) -> None:
        with self.lock:
            self.path.write_text(
                json.dumps(data, indent=2, ensure_ascii=False),
                encoding="utf-8",
            )

    def next_id(self, data: list[dict]) -> int:
        return max((b["id"] for b in data), default=0) + 1


def get_file() -> JsonStore:
    return JsonStore("books.json")