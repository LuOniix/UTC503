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


**Install the PIL package and the numpy package with the following commands:**

>> pip install pil

>> pip install numpy


**To launch the program**

>> python lsb.py


**Mode ⇒ Image encoding**

Choose the png image in which you want to hide your message. Then choose your message to hide.


**Mode ⇒ Image decoding**

Choose the png image to find the hidden message

	

Lucy Gastebois