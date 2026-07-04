from models import Item
from inventory import total_value


def audit_stock(raw_rows):
    """raw_rows come straight from the warehouse CSV export."""
    items = [Item(r["name"], r["price"], r["qty"]) for r in raw_rows]
    return total_value(items)


if __name__ == "__main__":
    rows = [
        {"name": "washer", "price": 0.1, "qty": 5000},
        {"name": "screw", "price": 0.3, "qty": 2200},
    ]
    print(f"Audit total: ${audit_stock(rows):.2f}")
