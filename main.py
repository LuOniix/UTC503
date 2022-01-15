# Import 
from email.mime import image
import numpy as np
from PIL import Image


# Cette fonction permet de récupérer les informations de l'image (dimensions et les pixels)
# :param, image 
# :return, arrayPixel, widthImg, heightImg 

def imageInformations(image):
    img = Image.open(image)
    widthImg, heightImg = img.size
    arrayPixel = np.array(list(img.getdata()))   # Récupère chaque pixel dans un tableau
    total_pixel = arrayPixel.size//3             # Récupèration de la total des pixel, divisé par 3 (car RGB sur 3 octets)
    return arrayPixel, widthImg, heightImg, total_pixel

# Cette fonction permet de passer le message ASCII en binaire

def ascii_to_binary(message):
    message += "$3nd0"                                              # délimiter pour marquer le message et le trouver
    binary = ' '.join(format(ord(c), 'b') for c in message)
    print("The Binary Representation is:", binary)
    len_msg = len(binary)
    return binary, len_msg

# Cette fonction permet de passer le message binaire en ASCII

def binary_to_ascii(message):
    n = int(message, 2)
    ascii = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
    print("The ASCII Representation is:",ascii )
    return message



# Cette fonction permet d'encoder le texte dans l'image 
# tab : le tableau des pixels
# les dimensions
# message 
# dest : le nom de l'image à la sortie 

def encode(tab, width, height, totalPix, message, dest):
    msg, len_msg = ascii_to_binary(message)             # appel de la fonction 

    if(len_msg > totalPix):
        print(" ERROR encode : message too long !")
        exit(10)
    
    else:
        cmpt = 0                                         # Compte les pixels 



# Cette fonction permet de décoder le texte dans l'image 


def main():

    print("\n === LSB === \n")

    img = input("Veuillez renseigner le chemin de l'image svp : " )
    arrayPixel, widthImg, heightImg, total_pixel = imageInformations(img)
    print("\nDimension de l'image :", widthImg, " x ", heightImg)
    print("Total de Pixels : ", total_pixel)

    message = input("\n Veuillez saisir le message à dissimuler : ")
    ascii_to_binary(message)


if __name__ == '__main__':
    main()

