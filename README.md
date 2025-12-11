                                   CARTOONIZATION OF IMAGE 
                                   ........................


Description:

       The image is first loaded using OpenCV and converted from BGR to RGB.

       A median blur with n=5 is applied.

       A lookup table is created to quantize pixel intensities into 5 discrete levels for a posterization effect.

       The LUT is applied channel wise (R, G, B) to the blurred image to obtain the cartoonized output.

       Matplotlib is used to show the original and cartoonized images side by side.

       OpenCV saves the final cartoonized image as a JPG file.​


Steps To RUN:

      Install Python 3 and the required libraries in the environment. 
      
      Run the main script from the root of the project folder.


Screenshots or output images:
    
         input image: vijay.png

         output image: cartoonizedimage.jpg