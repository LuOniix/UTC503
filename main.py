# Imports 
from array import array
from email.mime import image
import numpy as np
from PIL import Image


# This function allows you to retrieve information about the image (dimensions and pixels)
# :param : image 
# :return : arrayPixel, widthImg, heightImg 

def imageInformations(image):
    img = Image.open(image)
    #img.show()
    widthImg, heightImg = img.size
    arrayPixel = np.array(list(img.getdata()))                                  # Get each pixel in an array
    total_pixel = arrayPixel.size//3                                            # Total pixels divided by 3 because RGB on 3 bytes
    return arrayPixel, widthImg, heightImg, total_pixel

# This function allows to pass the ASCII message in binary
# :param : message 
# :return : binary, len_msg; the message in binary and its length

def ascii_to_binary(message):
    message += "$3nd0"                                                          # end marker 
    binary = ' '.join(format(ord(c), 'b') for c in message)
    #print("The Binary Representation is:", binary)
    len_msg = len(binary)
    return binary, len_msg

# This function allows to pass the binary message in ASCII
# :param : message 
# :return :

def binary_to_ascii(message):
    n = int(message, 2)
    ascii = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
    print("The ASCII Representation is:",ascii )
    return message



# This function allows to encode the text in the image 
# :param : tab, the pixel table 
# :param : width, image size 
# :param : height, image size 
# :param : totalPix, 
# :param : message, 
# :param : dest, name of the output image
# :return : 

def encode(tab, width, height, totalPix, message, dest):
    msgBinary, len_msg = ascii_to_binary(message)                               # call of the function

    if(len_msg > totalPix):                                                     # Checks if the message can be hidden in the image 
        print(" ERROR encode : message too long !")
        exit(10)
    
    else:
        cmpt = 0                                                                # Compte les pixels 
        for i in range(totalPix) :                                              # Browse the pixel array
            for j in range(3) :                                                 # Browse the bits for RGB 

                if(cmpt < len_msg) :                                            # We stop when the whole message is hidden 

                    tab[i][j] = int(bin(tab[i][j])[2:9]+ msgBinary[cmpt], 2)    # One puts in binary the element of the table then one recovers the 2nd bit at the 8th bit 
                                                                                # (one does not touch the bit of strong point) and one adds a bit of the message to him 
                    cmpt += 1
                    
        tab = tab.reshape(height, width, 3)                                     # Gives a new shape to an array without changing its data
        encoding_image = Image.fromarray(tab.astype('uint8'), 'RGB')            # Save a numpy table in image format
        encoding_image.save(dest)
        encoding_image.show()
        print(" >> Encoded image << ")      


# This function allows to decode the text in the image 


# Program launcher

def main():

    print("\n === LSB encryptor === \n")

    img = input("Veuillez renseigner le chemin de l'image svp : " )
    arrayPixel, widthImg, heightImg, total_pixel = imageInformations(img)
    print("\nDimension de l'image :", widthImg, " x ", heightImg)
    print("Total de Pixels : ", total_pixel)

    message = input("\n Veuillez saisir le message à dissimuler : ")
    msgBinary, len_msg = ascii_to_binary(message)
    print("La représentation binaire est :", msgBinary)

    dest = input("\n Veuillez saisir le nom de l'image encoder (doit se terminer par .jpg) : ")
    encode(arrayPixel, widthImg, heightImg, total_pixel, message, dest)



# Calling the launch function

if __name__ == '__main__':
    main()

