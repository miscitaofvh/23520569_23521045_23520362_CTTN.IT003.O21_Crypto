from PIL import Image, ImageChops

img1 = Image.open("flag.png")
img2 = Image.open("lemur.png")

img3 = ImageChops.difference(img1, img2)

img3.show()
img3.save("xor.png")