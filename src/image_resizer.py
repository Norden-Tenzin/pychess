from PIL import Image
from constants import *

if __name__ == "__main__":
    image = Image.open("./assets/pieces.png")
    width = image.width
    height = image.height 
    w_pointer = 0 
    h_pointer = 0 
    w_diff = (width/6)
    h_diff = (height/2)

    resized_size = (int(SIZE/8),int(SIZE/8))
    print(resized_size)

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