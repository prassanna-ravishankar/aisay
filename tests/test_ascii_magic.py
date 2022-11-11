from utils import test_dir
import ascii_magic
from PIL import Image

def test_image2ascii():
    temp_img = Image.open(test_dir() / "data/example_moon.png")
    my_art = ascii_magic.from_image(temp_img)
    with open(str(test_dir() / 'data/gt_ascii_data.txt'), "r") as f:
        gt_art = f.read()
    assert my_art == gt_art, "Ascii generation doesnt match"