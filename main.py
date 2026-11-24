# Funniest Autocorrect Fail — one line, 36 characters.
# Writes the line to /output/entry.txt (MAKEFUN_OUTPUT_DIR overrides,
# ./output is the local fallback). Python stdlib only, no network,
# fully deterministic (same bytes on every run).
import os

LINE = "I defrosted the children for dinner."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
    except OSError:
        out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
