from matplotlib import pylab
from matplotlib import pyplot as plt
import pydicom
import numpy as np
import random
import skimage
from skimage import filters
from skimage.segmentation import watershed
from funciones_p2 import *
from imimposemin import *

def WatershedExercise(imagen_normalizada, imagen_sobel, coord_sem): 
    '''
    Addition of Gaussian noise.
    
    Parameters:
        normalised_image : pixel array of the normalised image.
        sobel_image : pixel array of the sobel filtered image.
        coord_sem : list of seed coordinates.
        
    Returns:
        img_ws1 : pixel array resulting from the Watershed application. The imimposemin function has been applied to the image. 
        img_ws2 : matrix of pixels resulting from the application of Watershed. The image is the one with sobel filter.
    
    Notes:
        The array of zeros of the size of the original image is created. The image is then clicked on, the seed coordinates are calculated and the 
        the coordinates of the seeds are calculated and the pixels that are in the coordinates of the seeds are brought to white,
        in this case, in the matrix of zeros created.
        The algorithms imimposemin (on the sobel and binary image) and watershed (on the imimposemin and sobel image) are applied.
        and sobel). Finally, the result of the imimposemin function on the normalised and binary image is displayed on the screen. 
    '''

    img_binaria = np.zeros(imagen_normalizada.shape)

    for elem in range (len(coord_sem)):
        coord = coord_sem[elem]
        fila = coord[0] 
        col = coord[1]
        img_binaria[fila][col] = 1 #The seed coordinate is set to 1.
        
    min_loc = imimposemin(imagen_sobel, img_binaria) #Local minima
    img_ws1 = watershed(min_loc)
    img_ws2 = watershed(imagen_sobel)
    
    min_norm = imimposemin(imagen_normalizada, img_binaria)
    plt.figure(figsize=[8,6]) 
    plt.imshow(min_norm,cmap=pylab.cm.gray)
    plt.title('IMIMPOSEMIN en NORMALIZADA')

    return img_ws1, img_ws2
