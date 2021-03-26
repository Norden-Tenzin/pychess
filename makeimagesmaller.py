from PIL import Image
from constants import *

width = 2000
print(width/6)

height = 667 
print(height/2)

w_pointer = 0 
h_pointer = 0 

w_diff = (width/6)
h_diff = (height/2)

image = Image.open("./assets/pieces.png")
resizeSize = (int(SIZE/8),int(SIZE/8))
print(resizeSize)

# white
# king queen bishop knight rook pawn
cropped_image = image.crop((w_pointer, h_pointer, w_diff, h_diff))
resized = cropped_image.resize(resizeSize)
resized.save("./assets/w_king.png")

cropped_image1 = image.crop(((w_pointer + w_diff), h_pointer, (w_diff*2), h_diff))
resized = cropped_image1.resize(resizeSize)
resized.save("./assets/w_queen.png")
    
cropped_image2 = image.crop(((w_pointer + (w_diff*2)), h_pointer, (w_diff*3), h_diff))
resized = cropped_image2.resize(resizeSize)
resized.save("./assets/w_bishop.png")

cropped_image3 = image.crop(((w_pointer + (w_diff*3)), h_pointer, (w_diff*4), h_diff))
resized = cropped_image3.resize(resizeSize)
resized.save("./assets/w_knight.png")

cropped_image4 = image.crop(((w_pointer + (w_diff*4)), h_pointer, (w_diff*5), h_diff))
resized = cropped_image4.resize(resizeSize)
resized.save("./assets/w_rook.png")

cropped_image5 = image.crop(((w_pointer + (w_diff*5)), h_pointer, (w_diff*6), h_diff))
resized = cropped_image5.resize(resizeSize)
resized.save("./assets/w_pawn.png")

#black
# king queen bishop knight rook pawn

cropped_image = image.crop((w_pointer, h_diff, w_diff, h_diff*2))
resized = cropped_image.resize(resizeSize)
resized.save("./assets/b_king.png")

cropped_image1 = image.crop(((w_pointer + w_diff), h_diff, (w_diff*2), h_diff*2))
resized = cropped_image1.resize(resizeSize)
resized.save("./assets/b_queen.png")
    
cropped_image2 = image.crop(((w_pointer + (w_diff*2)), h_diff, (w_diff*3), h_diff*2))
resized = cropped_image2.resize(resizeSize)
resized.save("./assets/b_bishop.png")

cropped_image3 = image.crop(((w_pointer + (w_diff*3)), h_diff, (w_diff*4), h_diff*2))
resized = cropped_image3.resize(resizeSize)
resized.save("./assets/b_knight.png")

cropped_image4 = image.crop(((w_pointer + (w_diff*4)), h_diff, (w_diff*5), h_diff*2))
resized = cropped_image4.resize(resizeSize)
resized.save("./assets/b_rook.png")

cropped_image5 = image.crop(((w_pointer + (w_diff*5)), h_diff, (w_diff*6), h_diff*2))
resized = cropped_image5.resize(resizeSize)
resized.save("./assets/b_pawn.png")