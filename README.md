## | Project explanation |

The objective of the program is to hide information within an image.
This is the principle of steganography.
The steganography method known as LSB consists of manipulating the low-order bits of an image in order to hide information in it without altering its appearance.


The program works only on RGB pixels (it does not take into account RGBA pixels).
The use of an image in .png extension is necessary for the good functioning of the program.

  
## | Project statue |

The program is functional for images with .png extension.
The user can encode a message in an image as well as decode it.

/!\ Note that the decoding function only works if the user has used the encoding function of the program.


## | Installation and use of the project |


>> pip3 install -r requirements.txt

    Dependencies :
        - numpy
        - pillow


**To launch the program**

>> python3 lsb.py


**Tutorial**


**Mode ⇒ Image encoding**

Choose the png image in which you want to hide your message. Then choose your message to hide.

 ![Encoding](http://image.noelshack.com/fichiers/2022/04/2/1643133790-capture-d-ecran-1.png "Encoding").



**Mode ⇒ Image decoding**

Choose the png image to find the hidden message

 ![Decoding](http://image.noelshack.com/fichiers/2022/04/2/1643133790-capture-d-ecran-2.png)

**ERROR**

The user is required to enter the value "1" or "2" and an image with the extension .png.

 ![Error](http://image.noelshack.com/fichiers/2022/04/2/1643133790-capture-d-ecran-erreur.png)

Lucy 