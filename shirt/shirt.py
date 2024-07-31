import sys
import os
from PIL import Image, ImageOps


if len(sys.argv) < 3:
    sys.exit('Too few command-line arguments')
elif len(sys.argv) > 3:
    sys.exit('Too many command-line arguments')
elif sys.argv[1].split('.')[-1] not in ['jpg', 'jpeg', 'png']:
    sys.exit('Invalid input')
elif sys.argv[2].split('.')[-1] not in ['jpg', 'jpeg', 'png']:
    sys.exit('Invalid output')
elif sys.argv[1].split('.')[-1] != sys.argv[2].split('.')[-1]:
    sys.exit('Input and output have different extensions')
elif not(os.path.exists(sys.argv[1])):
    sys.exit('Input does not exist')

shirtImage = Image.open("shirt.png")

#with Image.open(sys.argv[2]) as outImage:
with Image.open(sys.argv[1]) as inImage:
    outImage = ImageOps.fit(inImage, shirtImage.size)
    outImage.paste(shirtImage, shirtImage)
    outImage.save(sys.argv[2])


