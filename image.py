from PIL import Image, ImageFilter

img = Image.open("./pokedex/pikachu.jpg")
filter_img = img.filter(ImageFilter.BLUR)
filter_img1 = img.filter(ImageFilter.SMOOTH_MORE)
filter_img2 = img.filter(ImageFilter.SHARPEN)
filter_img.save("blur.png", "png")
filter_img1.save("smooth.png", "png")
filter_img2.save("sharp.png", "png")

print(img)
print(img.format)
print(img.mode)
print(dir(img))