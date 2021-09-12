import cv2
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
from pylab import *
from PIL import Image
from copy import deepcopy

img_terang = cv2.imread("terang.jpg")
img_sedang = cv2.imread("sedang.jpg")
img_gelap = cv2.imread("gelap.jpg")

resized = (400,600)
img1 = cv2.resize(img_terang, resized)
img2 = cv2.resize(img_sedang, resized)
img3 = cv2.resize(img_gelap, resized)

def lihat_foto(img1,img2,img3):
    img = img1
    print("""
        Menu Lihat Foto Asli
    1. Foto Terang
    2. Foto Sedang
    3. Foto Gelap
    """)
    ch_lihat = input("Pilih: ")
    
    if ch_lihat == '1':
        cv2.imshow("Foto Terang", img1)
        cv2.waitKey(0)
        img = img1
    elif ch_lihat == '2':
        cv2.imshow("Foto Sedang", img2)
        cv2.waitKey(0)
        img = img2
    elif ch_lihat == '3':
        cv2.imshow("Foto Gelap", img3)
        cv2.waitKey(0)
        img = img3
    else:
        print("Pilihan Tidak Tersedia")

def rgb_channel(img):
    red_channel = deepcopy(img)
    green_channel = deepcopy(img)
    blue_channel = deepcopy(img)

    red_channel[:,:,1] = 0
    red_channel[:,:,2] = 0

    green_channel[:,:,0] = 0
    green_channel[:,:,2] = 0

    blue_channel[:,:,0] = 0
    blue_channel[:,:,1] = 0

    fig, ax = plt.subplots(ncols=2, nrows=2, figsize=(10,15))

    ax[0,0].imshow(img)
    ax[0,0].set_title('Original')

    ax[0,1].imshow(red_channel)
    ax[0,1].set_title('Red Channel')

    ax[1,0].imshow(green_channel)
    ax[1,0].set_title('Green Channel')

    ax[1,1].imshow(blue_channel)
    ax[1,1].set_title('Blue Channel')

    cv2.imwrite("hasil rgb/redchannel.jpg", blue_channel)
    cv2.imwrite("hasil rgb/greenchannel.jpg", green_channel)
    cv2.imwrite("hasil rgb/bluechannel.jpg", red_channel)

    plt.show()

def lihat_rgb():
    print("""
        Menu Lihat Foto Per-Channel RGB
    1. Foto Terang
    2. Foto Sedang
    3. Foto Gelap
    """)
    ch_lihat = int(input("Pilih : "))
    
    if ch_lihat==1:
        rgb_channel(img_terang)
    elif ch_lihat==2:
        rgb_channel(img_sedang)
    elif ch_lihat==3:
        rgb_channel(img_gelap)
    else:
        print("tidak ada")

def histogram(img, bins, title):
    plt.hist(img.ravel(),bins,[0,256]);
    plt.title(title)
    plt.show()

def histo_256bins():
    figure(0)
    histogram(img1,256,"Histogram Foto Terang")
    figure(1)
    histogram(img2,256,"Histogram Foto Sedang")
    figure(2)
    histogram(img3,256,"Histogram Foto Gelap")

def histo_rgb(bins):
    red = cv2.imread("hasil rgb/redchannel.jpg")
    green = cv2.imread("hasil rgb/greenchannel.jpg")
    blue = cv2.imread("hasil rgb/bluechannel.jpg")

    print('''
        Menu Warna
    1. Red
    2. Green
    3. Blue
    ''')

    choose = int(input("Pilih: "))
    if choose==1:
        histogram(red,bins,"Red")
    elif choose==2:
        histogram(green,bins,"Green")
    elif choose==3:
        histogram(blue,bins,"Blue")

def rgb_bins():
    print("""
    1. 4 bins
    2. 8 bins
    3. 16 bins
    4. 32 bins
    """)
    ch_bins = int(input("Pilih: "))

    if ch_bins==1:
        histo_rgb(4)
    elif ch_bins==2:
        histo_rgb(8)
    elif ch_bins==3:
        histo_rgb(16)
    elif ch_bins==4:
        histo_rgb(32)

def rgb_bins(image, bins):
    img = Image.open(image)
    lebar, tinggi = (img.size)

    listR = []
    listG = []
    listB = []

    for x in range(lebar):
        for y in range(tinggi):
            r, g, b = img.getpixel((x,y))
            listR.append(r)
            listG.append(g)
            listB.append(b)

    fig, axs = plt.subplots(1, 4, figsize=(20,5))
    axs[0].set_title("Foto Terang")
    axs[0].imshow(img)
    axs[1].set_title("Histogram Channel R")
    axs[1].hist(listR, bins, facecolor='red', alpha=0.5)
    axs[2].set_title("Histogram Channel G")
    axs[2].hist(listG, bins, facecolor='green', alpha=0.5)
    axs[3].set_title("Histogram Channel B")
    axs[3].hist(listB, bins, facecolor='blue', alpha=0.5)
    plt.show()

def histo_bins():
    print('''
    1. 4 bins
    2. 8 bins
    3. 16 bins
    4. 32 bins
    ''')
    choose = int(input("Pilih: "))

    if choose==1:
        rgb_bins("terang.jpg", 4)
    elif choose==2:
        rgb_bins("terang.jpg", 8)
    elif choose==3:
        rgb_bins("terang.jpg", 16)
    elif choose==4:
        rgb_bins("terang.jpg", 32)

def main():
    print('''
        Main Menu:
    1. Lihat Foto Asli
    2. Lihat Konversi Warna
    3. Lihat Foto Per-Channel RGB
    4. Lihat Histogram 256 Bins
    5. Lihat Histogram R,G,B
    6. Keluar
    ''')
    ch_main = input("Pilih: ")

    if ch_main == '1':
        lihat_foto(img1,img2,img3)
        cv2.destroyAllWindows
    elif ch_main == '2':
        pass
    elif ch_main == '3':
        lihat_rgb()
    elif ch_main == '4':
        histo_256bins()
    elif ch_main == '5':
        rgb_bins()
    elif ch_main == '6':
        exit(0)
    else:
        print("Pilihan Tidak Tersedia")

main()