from PIL import Image
import sys
from pathlib import Path

def main():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    in_path, out_path = sys.argv[1], sys.argv[2]
    in_ext, out_ext =Path(in_path).suffix, Path(out_path).suffix

    if out_ext.lower() in ['.jpg', '.jpeg', '.png']:
        if in_ext != out_ext:
            sys.exit("Input and output have different extensions")
        try:
            process(in_path, out_path)
        except FileNotFoundError:
            sys.exit('Input does not exist')
    else:
        sys.exit("Invalid output")

def process(in_path, out_path):
    shirt = Image.open("shirt.png")
    size = shirt.size
    photo = Image.open(in_path)

