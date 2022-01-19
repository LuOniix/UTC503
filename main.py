# Imports 
from array import array
from email.mime import image
import numpy as np
from PIL import Image


# This function allows you to retrieve information about the image (dimensions and pixels)
# :param : image 
# :return : arrayPixel, widthImg, heightImg 

def image_informations(image):
    img = Image.open(image)
    #img.show()
    width_Img, height_Img = img.size
    array_Pixel = np.array(list(img.getdata()))                                  # Get each pixel in an array
    total_pixel = array_Pixel.size//3                                            # Total pixels divided by 3 because RGB on 3 bytes
    return array_Pixel, width_Img, height_Img, total_pixel

# This function allows to pass the ASCII message in binary
# :param : message 
# :return : binary, len_msg; the message in binary and its length

def ascii_to_binary(message):
    message += "$3nd0"                                                           # end marker 
    binary = ' '.join(format(ord(c), 'b') for c in message)
    #print(f'The Binary Representation is: {binary}')
    len_msg = len(binary)
    return binary, len_msg

# This function allows to pass the binary message in ASCII
# :param : message 
# :return :

def binary_to_ascii(message):               # Ne fonctione pas, à revoir 
    n = int(message, 2)
    ascii = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
    print(f'The ASCII Representation is: {ascii}')
    return message



# This function allows to encode the text in the image 
# :param : tab, the pixel table 
# :param : width, image size 
# :param : height, image size 
# :param : totalPix, 
# :param : message, 
# :param : dest, name of the output image

def encode(tab, width, height, total_Pixel, message, dest):
    msgBinary, len_msg = ascii_to_binary(message)                               # call of the function

    if(len_msg > total_Pixel):                                                  # Checks if the message can be hidden in the image 
        print(f' /!\ ERROR encode : message too long !')
        exit(10)
    
    else:
        cmpt = 0                                                                # Compte les pixels 
        for i in range(total_Pixel) :                                           # Browse the pixel array
            for j in range(3) :                                                 # Browse the bits for RGB 

                if(cmpt < len_msg) :                                            # We stop when the whole message is hidden 

                    tab[i][j] = int(bin(tab[i][j])[2:9]+ msgBinary[cmpt], 2)    # One puts in binary the element of the table then one recovers the 2nd bit at the 8th bit 
                                                                                # (one does not touch the bit of strong point) and one adds a bit of the message to him 
                    cmpt += 1
                    
        tab = tab.reshape(height, width, 3)                                     # Gives a new shape to an array without changing its data
        encoding_image = Image.fromarray(tab.astype('uint8'), 'RGB')            # Save a numpy table in image format
        encoding_image.save(dest)
        encoding_image.show()
        print(f'Loading ... ')  


# This function allows to decode the text in the image 

def decode (tab, total_Pixel):

    bits_hidden = ""
    for i in range(total_Pixel) :                                                # Browse the pixel array
        for j in range(3) :                                                      # Browse the bits for RGB 

            bits_hidden += (bin(tab[i][j]) [2:][-1])                             # Gets the hidden bits at the end of the line (low-bit)
    
       


            end_marker = ""
            message = ""



    return message

# Program launcher

def main():

    print(f'\n===  LSB Encrytor ===\n')
    print(f'\n Les modes : \n')
    print(f'\n1- Encoder')
    print(f'2- Décoder\n')

    choose = input("Veuillez choisir le mode (1 ou 2) : ")

    if( choose == "1") :

        print(f'\n Mode => Encodage de l image \n')
        img = input("Veuillez renseigner le chemin de l'image svp : " )         # Vérifier l'entrée saisie !
        array_Pixel, width_Img, height_Img, total_pixel = image_informations(img)
        print(f'\nDimension de l image : {width_Img} X {height_Img}')
        print(f'Total de Pixels : {total_pixel}')
    
        message = input("\n Veuillez saisir le message à dissimuler : ")
        msg_Binary, len_msg = ascii_to_binary(message)
        print(f'La représentation binaire est : {msg_Binary}')
        binary_to_ascii(msg_Binary)

        dest = input("\n Veuillez saisir le nom de la nouvelle image encoder : ")
        encode(array_Pixel, width_Img, height_Img, total_pixel, message, dest)
        print(f'\n >> Image encodée << \n')
    
    elif( choose == "2") :
        
        print(f'\n Mode => Décodage de l image \n')
        img = input("Veuillez renseigner le chemin de l'image svp : " )  
        array_Pixel, width_Img, height_Img, total_pixel = image_informations(img)
        print(f'\nDimension de l image : {width_Img} X {height_Img}')
        print(f'Total de Pixels : {total_pixel}')  

        message = decode(array_Pixel, total_pixel)
        print(f'\n >> Image décodée << \n')
        print(f'\n >> Le message dissumulée dans l image est : {message}')

    else : 
        print(f'\n /!\ Erreur de saisie ! \n Redémarrez le programme ... \n')



# Calling the launch function

if __name__ == '__main__':
    main()

