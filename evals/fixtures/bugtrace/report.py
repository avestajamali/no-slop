import json
import os

from models import Item
from inventory import total_value

CACHE = os.path.join(os.path.dirname(__file__), "cache.json")


def load_items():
    if os.path.exists(CACHE):
        with open(CACHE) as f:
            return json.load(f)
    items = [Item("bolt", 0.5, 1200), Item("nut", 0.2, 3400)]
    with open(CACHE, "w") as f:
        json.dump([i.to_dict() for i in items], f)
    return items


def weekly_report():
    items = load_items()
    return f"Total inventory value: ${total_value(items):.2f}"


if __name__ == "__main__":
    print(weekly_report())
