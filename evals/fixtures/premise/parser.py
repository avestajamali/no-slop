def parse_line(line):
    return line.rstrip("\n").split(",")


def load(path):
    with open(path) as f:
        header = parse_line(f.readline())
        return [dict(zip(header, parse_line(row))) for row in f]
