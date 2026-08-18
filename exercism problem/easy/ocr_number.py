#copy-pasted from glm5 turbo ai...yeh toh mai kar hi nahi paya yaar...
import sys

DIGIT_GRID = {
    0: ["   ", "| |", "|_|", "   "],
    1: ["   ", "  |", "  |", "   "],
    2: [" _ ", " _|", "|_ ", "   "],
    3: [" _ ", " _|", " _|", "   "],
    4: ["   ", "|_|", "  |", "   "],
    5: [" _ ", "|_ ", " _|", "   "],
    6: [" _ ", "|_ ", "|_|", "   "],
    7: [" _ ", "  |", "  |", "   "],
    8: [" _ ", "|_|", "|_|", "   "],
    9: [" _ ", "|_|", " _|", "   "]
}

GRID_TO_DIGIT = {tuple(rows): num for num, rows in DIGIT_GRID.items()}

data = sys.stdin.read().rstrip("\n")

if data:
    if "\n" in data:
        lines = data.split("\n")[:4]
        while len(lines) < 4:
            lines.append("")
        w = max(len(l) for l in lines)
        n = w // 3
        padded_lines = [l.ljust(n * 3) for l in lines]
        out = []
        for i in range(n):
            s = tuple(padded_lines[r][i*3:i*3+3] for r in range(4))
            out.append(str(GRID_TO_DIGIT.get(s, "?")))
        print("".join(out))
    else:
        digits = [int(c) for c in data if c.isdigit()]
        print()
        for r in range(4):
            print("".join(DIGIT_GRID[d][r] for d in digits))

#solution...

DIGIT_STRINGS = [
    ' _ | ||_|   ',  # 0
    '     |  |   ',  # 1
    ' _  _||_    ',  # 2
    ' _  _| _|   ',  # 3
    '   |_|  |   ',  # 4
    ' _ |_  _|   ',  # 5
    ' _ |_ |_|   ',  # 6
    ' _   |  |   ',  # 7
    ' _ |_||_|   ',  # 8
    ' _ |_| _|   ',  # 9
]

W, H = 3, 4


def convert(input_grid):
    # an OCR "line" is a list of 4 lines of text
    ocr_lines = validate(input_grid)
    return ','.join(
        scan_ocr_line(line)
        for line in ocr_lines
    )


def scan_ocr_line(line):
    digit_strings = [
        ''.join(l[i:i+W] for l in line)
        for i in range(0, len(line[0]), W)
    ]
    return ''.join(
        str(DIGIT_STRINGS.index(d)) if d in DIGIT_STRINGS else '?'
        for d in digit_strings
    )


def validate(grid):
    if len(grid) % H != 0:
        raise ValueError('Number of input lines is not a multiple of four')
    ocr_lines = [grid[i:i+H] for i in range(0, len(grid), H)]
    for lines in ocr_lines:
        if any(map(lambda x: len(x) % W != 0, lines)):
            raise ValueError(f'Number of input columns is not a multiple of three')
    return ocr_lines