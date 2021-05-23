import cv2 as cv
from skimage import io
from utils import binarizar, gerar_imagem_contornada
from operacoes import dilatar, erodir, abertura, fechamento
caminho_imagens = "./assets/"

imagem_original = cv.cvtColor(io.imread(caminho_imagens + "img02.png"), cv.COLOR_RGBA2GRAY)
imagem_binaria = binarizar(imagem_original)

img_contornada = gerar_imagem_contornada(imagem_binaria)

elemento_estruturante = cv.getStructuringElement(cv.MORPH_ELLIPSE, (15,15))

#cv.imshow('Imagem Original', imagem_binaria)

"""
SEÇÃO DAS OPERAÇÕES DE DILATAÇÃO E EROSÃO
"""
img_dilatada = dilatar(imagem_binaria, elemento_estruturante, img_contornada)
cv.imshow('Imagem Dilatada', img_dilatada)

img_erodida = erodir(imagem_binaria, elemento_estruturante, img_contornada)
cv.imshow('Imagem Erodida', img_erodida)

"""
SEÇÃO DAS OPERAÇÕES ABERTURA E FECHAMENTO
"""
img_abertura = abertura(imagem_binaria, elemento_estruturante, img_contornada)
cv.imshow('Abertura', img_abertura)

img_fechamento = fechamento(imagem_binaria, elemento_estruturante, img_contornada)
cv.imshow('Fechamento', img_fechamento)

cv.waitKey(0)