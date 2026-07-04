import os

from parser import load

HERE = os.path.dirname(os.path.abspath(__file__))


def contacts():
    rows = load(os.path.join(HERE, "data.csv"))
    return [f"{r['company']}: {r['contact']}" for r in rows]


if __name__ == "__main__":
    for line in contacts():
        print(line)
