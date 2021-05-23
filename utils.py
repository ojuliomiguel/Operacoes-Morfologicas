import numpy as np
from skimage.measure import find_contours
import cv2 as cv

def binarizar(image):
    imagem_bin = np.zeros(image.shape)
    for i in range(len(image)):
        for j in range(len(image[0])):
            if image[i, j] != 0:
                imagem_bin[i, j] = 255
    
    resultado = np.copy(imagem_bin) 
    
    return resultado

def gerar_imagem_contornada(imagem):
    contornos_img = np.zeros(imagem.shape + (3, ), np.uint8)

    contornos = find_contours(imagem, 0)

    for contorno in contornos:

        contorno = contorno.astype(np.int).tolist()
        
        # desenhar linhas de contorno
        for idx, coords in enumerate(contorno[:-1]):
            y1, x1, y2, x2 = coords + contorno[idx + 1]
            contornos_img = cv.line(contornos_img, (x1, y1), (x2, y2),(0, 255, 0), 1)
        
    contornos_img = contornos_img[:,:,1]

    return contornos_img

