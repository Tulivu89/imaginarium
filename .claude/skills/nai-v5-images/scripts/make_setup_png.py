#!/usr/bin/env python3
"""Write a blank PNG carrying a NovelAI V5 setup in its metadata.

Drag the PNG into NovelAI's image generator and choose Import to load the
prompt, UC, character boxes and settings. On import, untick Seed unless the
setup pins one.

Usage:
    python3 make_setup_png.py setup.json out.png

setup.json:
{
  "title": "Mythic Overdrive rig base A",
  "base": "...", "uc": "...",
  "chars": [{"prompt": "...", "uc": "...", "x": 0.5, "y": 0.5}],
  "width": 832, "height": 1216, "steps": 28, "scale": 4.5,
  "cfg_rescale": 0.1, "sampler": "k_euler_ancestral",
  "noise_schedule": "karras", "seed": null, "use_coords": false
}
Character prompts may use line breaks; they are joined with spaces, as
NovelAI stores them. The metadata layout is copied from a real V5 image
(nai_v5_comment_template.json), minus its prompts, seed and signature.
"""
import json
import random
import sys
from pathlib import Path

from PIL import Image
from PIL.PngImagePlugin import PngInfo

TEMPLATE = Path(__file__).with_name("nai_v5_comment_template.json")


def flat(text):
    return " ".join(line.strip() for line in text.strip().splitlines() if line.strip())


def build(setup):
    c = json.loads(TEMPLATE.read_text())
    chars = setup.get("chars", [])
    base, uc = setup["base"].strip(), setup["uc"].strip()
    c["prompt"], c["uc"] = base, uc
    for key, default in (("width", 832), ("height", 1216), ("steps", 28),
                         ("scale", 4.5), ("cfg_rescale", 0.1),
                         ("sampler", "k_euler_ancestral"),
                         ("noise_schedule", "karras")):
        c[key] = setup.get(key, default)
    seed = setup.get("seed")
    c["seed"] = seed if seed is not None else random.randint(0, 2**32 - 1)
    use_coords = bool(setup.get("use_coords", False))
    c["v4_prompt"]["use_coords"] = use_coords
    c["v4_prompt"]["caption"] = {
        "base_caption": base,
        "char_captions": [{"char_caption": flat(ch["prompt"]),
                           "centers": [{"x": ch.get("x", 0.5), "y": ch.get("y", 0.5)}]}
                          for ch in chars]}
    c["v4_negative_prompt"]["caption"] = {
        "base_caption": uc,
        "char_captions": [{"char_caption": flat(ch.get("uc", "")),
                           "centers": [{"x": ch.get("x", 0.5), "y": ch.get("y", 0.5)}]}
                          for ch in chars]}
    return c


def main(src, out):
    setup = json.loads(Path(src).read_text())
    comment = build(setup)
    info = PngInfo()
    info.add_text("Title", "NovelAI generated image")
    info.add_text("Description", comment["prompt"])
    info.add_text("Software", "NovelAI")
    info.add_text("Source", "NovelAI Diffusion V5 0ADF9AB7")
    info.add_text("Comment", json.dumps(comment, ensure_ascii=False))
    img = Image.new("RGB", (comment["width"], comment["height"]), (255, 255, 255))
    img.save(out, pnginfo=info, optimize=True)
    print(f"wrote {out} ({setup.get('title', '')}), seed {comment['seed']}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
