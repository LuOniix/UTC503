import sys
import numpy as np
from PIL import Image


def image_infos(image):
    """This function allows you to retrieve information about the image (dimensions and pixels).

    Args:
        image (str): the path of the image

    Returns:
        array_pixel, width_img, height_img
    """

    img = Image.open(image)
    width_img, height_img = img.size
    array_pixel = np.array(list(img.getdata()))                                  # Get each pixel in an array
    total_pixel = array_pixel.size//3                                            # Total pixels divided by 3 because RGB on 3 bytes
    return array_pixel, width_img, height_img, total_pixel


def ascii_to_binary(message):
    """This function allows to pass the ASCII message in binary.

    Args:
        message (str): the hidden message in ascii

    Returns:
        binary, len_msg; the message in binary and its length
    """
    message += "$3nd0"                                                           # end marker
    binary = ""
    for letter in message:
        binary += format(ord(letter), "08b")
    len_msg = len(binary)
    return binary, len_msg


def encode(tab, width, height, total_pixel, message, dest):
    """This function allows to encode the text in the image.

    Args:
        tab (tuple) : the pixel table
        width (int) : image size
        height (int) : image size
        total_pixel (int) : total number of pixels
        message (str) : hidden message
        dest (str) : name of the output image
    """
    msg_binary, len_msg = ascii_to_binary(message)                               # call of the function

    if len_msg > total_pixel:                                                  # Checks if the message can be hidden in the image
        print(' /!\ ERROR encode : message too long !')
        sys.exit(10)

    else:
        count = 0                                                               # Compteur pixels
        for i in range(total_pixel):                                           # Browse the pixel array
            for j in range(3):                                                 # Browse the bits for RGB

                if count < len_msg:                                            # We stop when the whole message is hidden

                    tab[i][j] = int(bin(tab[i][j])[:-1] + msg_binary[count], 2)  # (one does not touch the bit of strong point) and one adds a bit of the message to him
                    count += 1

        tab = tab.reshape(height, width, 3)                                     # Gives a new shape to an array without changing its data
        encoding_image = Image.fromarray(tab.astype('uint8'), 'RGB')            # Save a numpy table in image format
        encoding_image.save(dest)
        encoding_image.show()


def decode(tab, total_pixel):
    """This function allows to decode the text in the image.

    Args:
        tab (tuple) : the pixel table
        total_pixel (int) : total number of pixels

    Returns:
        (tuple) arrayPixel, (int) widthImg, (int) heightImg
    """

    bits_hidden = ""
    for i in range(total_pixel):                                                # Browse the pixel array
        for j in range(3):                                                      # Browse the bits for RGB

            bits_hidden += (bin(tab[i][j]) [2:][-1])                             # Gets the hidden bits at the end of the line (low-bit)

    bits_hidden = [bits_hidden[i:i+8] for i in range(0, len(bits_hidden), 8)]

    end_marker = "$3nd0"                                                         # end marker
    message = ""

    for i, value in enumerate(bits_hidden):                                           # We look for the end marker to find the message
        if message[-5:] == end_marker:
            break
        else:
            message += chr(int(value, 2))

    if end_marker in message:
        print(f'The hidden message is : {message[:-5]}')                         # If the hidden message is found, it is displayed
    else:
        print('There is no hidden message found')


def main():
    """This function allows to launch the program and to choose the mode (encode or decode).
    """

    print(" _       _____ ____    ______                       _               _______                             _             ")
    print("| |     / ____|  _ \  |  ____|                     | |             / /  __ \                           | |            ")
    print("| |    | (___ | |_) | | |__   _ __   ___ _ __ _   _| |_ ___  _ __ / /| |  | | ___  ___ _ __ _   _ _ __ | |_ ___  _ __ ")
    print("| |     \___ \|  _ <  |  __| | '_ \ / __| '__| | | | __/ _ \| '__/ / | |  | |/ _ \/ __| '__| | | | '_ \| __/ _ \| '__|")
    print("| |____ ____) | |_) | | |____| | | | (__| |  | |_| | || (_) | | / /  | |__| |  __/ (__| |  | |_| | |_) | || (_) | |   ")
    print("|______|_____/|____/  |______|_| |_|\___|_|   \__, |\__\___/|_|/_/   |_____/ \___|\___|_|   \__, | .__/ \__\___/|_|   ")
    print("                                               __/ |                                         __/ | |                  ")
    print("                                              |___/                                         |___/|_|                  ")
    print('\nChoose your mode  : \n')
    print('\n1- Encode')
    print('2- Decode\n')

    input_ok = False

    while not input_ok:

        choose = input("Please choose the mode (1 or 2) : ")

        if choose == "1":

            print('\nMode => Image encoding \n')
            img = input("Please enter the path of the image in .png : ")

            if img[-4:] == ".png":

                input_ok = True
                array_pixel, width_img, height_img, total_pixel = image_infos(img)
                print(f'\nImage size : {width_img} X {height_img}')
                print(f'Total Pixels : {total_pixel}')

                message = input("\nPlease enter the message to be hidden : ")
                msg_binary, len_msg = ascii_to_binary(message)
                print(f'The binary representation is : {msg_binary}')

                dest = input("\nPlease enter the name of the new image in .png encoder : ")
                encode(array_pixel, width_img, height_img, total_pixel, message, dest)
                print('\n >> Success! Encoded image << \n')

            else:
                print('\n /!\ Input Error : .png /!\ ')

        elif choose == "2":

            print('\nMode => Image decoding \n')
            img = input("Please enter the path of the image in .png : ")

            if img[-4:] == ".png":

                input_ok = True
                array_pixel, width_img, height_img, total_pixel = image_infos(img)
                print(f'\nImage size : {width_img} X {height_img}')
                print(f'Total Pixels : {total_pixel}')

                decode(array_pixel, total_pixel)
                print('\n >> Success ! Decoded image << \n')

            else:
                print('\n /!\ Input Error : .png /!\ \n')

        if not input_ok:
            print('\n /!\ Input Error /!\ \n >> restart your entry \n')

# Calling the launch function


if __name__ == '__main__':
    main()

