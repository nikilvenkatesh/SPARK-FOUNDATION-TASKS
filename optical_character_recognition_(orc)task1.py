# -*- coding: utf-8 -*-
"""Optical Character Recognition (ORC)TASK1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1e5SPhteGmWSioeOdRASAtbmdvv08iA-s

TASK 1:Optical Character Recognition (ORC)

PROBLEM STATEMENT:Character detector which extracts printed or handwritten text from an image or video.

NIKIL VENKATESH K

Computer Vision & Internet of Things

IMPORT LIBRARIES
"""

import cv2 as cv
import matplotlib.pyplot as plt

"""Install Pytesseract and tesseract-OCR in Google Colab."""

!sudo apt install tesseract-ocr
!pip install pytesseract

"""Import libraries"""

import pytesseract
import shutil
import os
import random
try:
 from PIL import Image
except ImportError:
 import Image

"""Upload Image to Colab"""

img = cv.imread("Ronaldo Quotes.jfif")
plt.imshow(img)

"""Convert image to grayscale"""

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
plt.imshow(gray)

"""Text Extraction"""

TXT=pytesseract.image_to_string(gray)
TXT