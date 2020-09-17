from PIL import Image, ImageFilter

img = Image.open("./pokedex/astro.jpg")
print(img.size)
new_img = img.resize\
    ((400, 400))
new_img.save("resize.png", "png")
print(new_img.size)
