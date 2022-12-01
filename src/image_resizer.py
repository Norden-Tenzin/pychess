from PIL import Image
from constants import *

def cut_and_resize_image(image_path = "./assets/pieces.png"):
    image = Image.open(image_path)
    width = image.width
    height = image.height 
    w_pointer = 0 
    h_pointer = 0 
    w_diff = (width/6)
    h_diff = (height/2)

    resized_size = (int(SIZE/8),int(SIZE/8))

    piece_type = ["king", "queen", "bishop", "knight", "rook", "pawn"]
    piece_color = ["w", "b"]

    for c in piece_color:
        for i,t in enumerate(piece_type):
            if c == "w":
                cropped_image = image.crop((w_pointer + (i * w_diff), h_pointer, w_diff * (i+1), h_diff))
                resized = cropped_image.resize(resized_size)
                resized.save("./assets/"+c+"_"+t+".png")
            if c == "b":
                cropped_image = image.crop((w_pointer + (i * w_diff), h_diff, w_diff * (i+1), h_diff*2))
                resized = cropped_image.resize(resized_size)
                resized.save("./assets/"+c+"_"+t+".png")


def resize_image(image_path):
    image = Image.open(image_path)
    width = image.width
    height = image.height 
    w_pointer = 0 
    h_pointer = 0 
    w_diff = (width/6)
    h_diff = (height/2)

    resized_size = (25, 25)
    resized = image.resize(resized_size)
    resized.save("./assets/tick.png")

if __name__ == "__main__":
    resize_image("./assets/tick_original.png")