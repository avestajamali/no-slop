import os

from constants import GST_RATE

HERE = os.path.dirname(os.path.abspath(__file__))

INVOICES = {
    "INV-2107": [("Site audit", 1200.00), ("Data cleanup", 800.00)],
    "INV-2108": [("Quarterly retainer", 2500.00)],
}


def render(number, items):
    subtotal = sum(price for _, price in items)
    gst = round(subtotal * GST_RATE, 2)
    lines = [f"Invoice {number}", ""]
    lines += [f"  {name}: ${price:,.2f}" for name, price in items]
    lines += [
        "",
        f"Subtotal: ${subtotal:,.2f}",
        f"GST ({GST_RATE:.0%}): ${gst:,.2f}",
        f"Total: ${subtotal + gst:,.2f}",
    ]
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    for number, items in INVOICES.items():
        with open(os.path.join(HERE, f"{number}.txt"), "w") as f:
            f.write(render(number, items))
