import numpy as np
from utils import gerar_imagem_contornada

def dilatar(imagem, elemento_estruturante, contornos_img):

        img_a_dilitar = imagem 

        # O c é uma espécie de correção para não aplicar o elemento estruturante errado
        c = int(len(elemento_estruturante)/2)  

        # Percorre a imagem
        for i in range(len(img_a_dilitar)):
            for j in range(len(img_a_dilitar[0])):

                #Se for uma borda, aplica-se logo mais o elemento estruturante com o pixel branco, por exemplo (255)
                if contornos_img[i, j] == 255:

                    for k in range(len(elemento_estruturante)):
                        for l in range(len(elemento_estruturante[0])):

                            # Confere se o elemento estruturante está contido na matriz
                            if elemento_estruturante[k, l] != 0:
                                try:
                                    # Aplicando a transformação - neste caso pintando de branco (dilatando). 
                                    img_a_dilitar[i + k - c, j + k - c] = 255
                                except:
                                    pass

        return img_a_dilitar  

def erodir(imagem, elemento_estruturante, contornos_img):
        
        img_a_erodir = imagem
        
        c = int(len(elemento_estruturante)/2) 

        for i in range(len(img_a_erodir)):
            for j in range(len(img_a_erodir[0])):

                if contornos_img[i, j] == 255:

                    for k in range(len(elemento_estruturante)):
                        for l in range(len(elemento_estruturante[0])):

                            if elemento_estruturante[k, l] != 0:
                                try:
                                    img_a_erodir[i + k - c, j + k - c] = 0
                                except:
                                    pass
        return img_a_erodir

def abertura(imagem, elemento_estruturante, contornos_img):
        img_copia = np.copy(imagem)
        img_erodida = erodir(img_copia, elemento_estruturante, contornos_img)
        contorno_novo = gerar_imagem_contornada(img_erodida)
        img_abertura = dilatar(img_erodida, elemento_estruturante, contorno_novo)

        return img_abertura

def fechamento(imagem, elemento_estruturante, contornos_img):
        img_copia = np.copy(imagem)
        img_dilatada = dilatar(img_copia, elemento_estruturante, contornos_img)
        contorno_novo = gerar_imagem_contornada(img_dilatada)
        img_fechamento = erodir(img_dilatada, elemento_estruturante, contorno_novo)

        return img_fechamento
