import os

TEXT = "My fridge updated its firmware overnight and now the crisper drawer requires two-factor authentication."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)

with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(TEXT)
