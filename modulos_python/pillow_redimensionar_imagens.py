# Pillow: redimensionando imagens com python
# Essa biblioteca é o Photoshop do python

from pathlib import Path

from PIL import Image

ROOT_FOLDER = Path(__file__).parent
ORIGINAL = ROOT_FOLDER / 'original.jpg'
NEW_IMAGE = ROOT_FOLDER / 'pedro_ganhou_meu_coracao.jpg'

pil_image = Image.open(ORIGINAL)
width, height = pil_image.size
#exif = pil_image.info['exif']

new_width = 4430
new_height = round(height * new_width / width)

new_image = pil_image.resize(size=(new_width, new_height))
new_image.save(
    NEW_IMAGE,
    optimize=True,
    quality=100,
    #exif=exif,
)