import PIL.Image


ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]


def muuta_koko(image, new_width=100):
    width, height = image.size
    ratio = height/width / 1.2
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return(resized_image)


def harmaannuta(image):
    grayscale_image = image.convert("L")
    return(grayscale_image)
    

def pixelista_askii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return(characters)    

def main(new_width=100):
    
    path = input("path:\n")
    try:
        image = PIL.Image.open(path)
    except Exception as e:
        print(path, f"{e}")
        return
  
    # convert image to ascii    
    uusi_data = pixelista_askii(harmaannuta(muuta_koko(image)))
    
    # format
    pixel_count = len(uusi_data)  
    ascii_image = "\n".join([uusi_data[index:(index+new_width)] for index in range(0, pixel_count, new_width)])
    
    # print result
    print(ascii_image)
    
    # save result to "ascii_image.txt"
    with open("ballerin taideteos.txt", "w") as f:
        f.write(ascii_image)
 
# run program
main()