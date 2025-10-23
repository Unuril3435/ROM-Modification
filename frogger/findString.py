import sys

# Build an array which describes how far away each byte is from the next
def getDifferences(x):
    return [x[i + 1] - x[i] for i in range(len(x) - 1)]

# Ensure correct usage
try:
    s = sys.argv[1].encode('utf-8')  # convert search string to bytes
    c = getDifferences(s)
except IndexError:
    sys.stdout.write(f"usage: {sys.argv[0]} \"search string\" file...\n")
    sys.exit(-1)

for fname in sys.argv[2:]:
    try:
        with open(fname, "rb") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"File not found: {fname}")
        continue

    print(f"looking for {s.decode('utf-8', errors='ignore')} in {fname}")

    for i in range(0, len(content) - len(s)):
        segment = content[i:i + len(s)]
        if getDifferences(segment) == c:
            print(f"\tmatch in {fname} at offset 0x{i:02x}")

