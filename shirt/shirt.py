from PIL import Image
import sys
from pathlib import Path

def main():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    img_in, img_out = sys.argv[1], sys.argv[2]
    if Path(img_in).suffix.lower() in ['.jpg', '.jpeg', '.png']:
        try:
            read_write(img_in, img_out)
        except FileNotFoundError:
            sys.exit(f"Could not read {file_name}")
    else:
        sys.exit("Not a CSV file")