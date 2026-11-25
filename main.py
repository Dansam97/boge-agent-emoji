import os

ENTRY = "\U0001fa9e"
MAX_CHARS = 16


def render():
    text = ENTRY
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError("entry must be 1-16 characters")
    if not text.strip():
        raise ValueError("entry must not be whitespace-only")
    text.encode("utf-8")
    return text


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(render())


if __name__ == "__main__":
    main()
