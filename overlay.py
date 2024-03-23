from itertools import zip_longest
from pdf2image import convert_from_path
from PIL import Image
import sys

# https://stackoverflow.com/a/75800059

pages = convert_from_path(sys.argv[1])
pages2 = convert_from_path(sys.argv[2])
                                                                                         
RESOLUTION = 300 # DPI
                                                                                        
new_pages = []
                                                                                        
for p1, p2 in zip_longest(pages, pages2):
    # Get the nth page of each pdf together
    if p1 is None:
        new_pages.append(p2)
    elif p2 is None:
       new_pages.append(p1)
    else:
        new_pages.append(Image.blend(p1, p2, alpha=0.5))

new_pages[0].save(
    "out.pdf", save_all=True, append_images=new_pages[1:], resolution=RESOLUTION
)
