from matplotlib.pyplot import ginput
from matplotlib import pylab
from matplotlib import pyplot as plt
import pydicom
import numpy as np
import math
from funciones_p2 import *


def RegionGrowing(img_norm, list_sem, umbral):
    '''
    Segmentation by growth regions.
    
    Parameters:
        image : normalised image matrix.
        list_sem : list of seed coordinates.
        threshold : determinant value of the range of greys included in the homogeneity criterion. 
        
    Returns:
        matrix_cr : matrix of the segmented image.
    
    Notes:
        The image is normalised and the seed coordinates are obtained. Then create
        an array of zeros of the size of the normalised image and set the clicked coordinate to 1. 
        where it has been clicked. The 8 neighbours are analysed iteratively until the pixels do not meet the condition.
        the condition.
    '''
    
    coord_sem = list_sem[0] 
    matriz_cr = np.zeros(img_norm.shape) 
    matriz_cr[coord_sem[0]][coord_sem[1]] = 1 
    pix_sem = img_norm[coord_sem[0]][coord_sem[1]] #Grey seed level.
    
    coord_homog = [] 
    coord_homog.append(coord_sem) 
    
    ya_comparadas = [] 
    ya_comparadas.append(coord_sem)
    
    while (len(coord_homog)!= 0):
        coordenada = coord_homog.pop(0) #Coordinate of the list that has been removed, is the pixel to be centred.
        for i in range(coordenada[0]-1, coordenada[0]+2): 
            for j in range (coordenada[1]-1, coordenada[1]+2): 
            #Coordinates with neighbourhood at 8 centred on the seed are taken.
                if ((0 <= i <= (img_norm.shape[0]-1)) and (0 <= j <= (img_norm.shape[1]-1))): 
                    pixel = img_norm[i][j]
                    c = (i,j)
                
                    if c not in ya_comparadas:
                        ya_comparadas.append(c)
                        if (pixel >= (pix_sem - umbral)) and (pixel <= (pix_sem + umbral)):
                        #In this if there are 3 conditions:
                            #1. If the pixel belongs to the interval.
                            #2. If the pixel is not outside the image boundaries.
                            #3. If the neighbour coordinate is NOT yet in already_compared.
                        
                            matriz_cr[i][j] = 1 
                            coord_homog.append(c)
                        
    return matriz_cr
