import cv2
from pylab import *
from copy import deepcopy
import matplotlib.pyplot as plt

# membaca gambar
img_terang = cv2.imread("Gambar/terang.jpeg")
img_sedang = cv2.imread("Gambar/sedang.jpeg")
img_gelap = cv2.imread("Gambar/gelap.jpeg")

# menampilkan gambar asli
def show_asli():
    fig, ax = plt.subplots(ncols=3, nrows=1, figsize=(20,10))

    ax[0].imshow(img_terang)
    ax[0].set_title('Foto Terang')
    ax[1].imshow(img_sedang)
    ax[1].set_title('Foto Sedang')
    ax[2].imshow(img_gelap)
    ax[2].set_title('Foto Gelap')

# fungsi untuk memecah gambar ke dalam berbagai channel (R,G,B) dan menyimpannya
def rgb_channel(img, jpg1, jpg2, jpg3):
    red_channel = deepcopy(img)
    green_channel = deepcopy(img)
    blue_channel = deepcopy(img)

    red_channel[:,:,1] = 0
    red_channel[:,:,2] = 0

    green_channel[:,:,0] = 0
    green_channel[:,:,2] = 0

    blue_channel[:,:,0] = 0
    blue_channel[:,:,1] = 0

    # menyimpan gambar ke device/database
    cv2.imwrite(jpg1, blue_channel)
    cv2.imwrite(jpg2, green_channel)
    cv2.imwrite(jpg3, red_channel)

# menyimpan photo per-channel ke dalam nama file tertentu
def rgb_photo():
    rgb_channel(img_terang, "Gambar/red_terang.jpeg", "Gambar/green_terang.jpeg", "Gambar/blue_terang.jpeg")
    rgb_channel(img_sedang, "Gambar/red_sedang.jpeg", "Gambar/green_sedang.jpeg", "Gambar/blue_sedang.jpeg")
    rgb_channel(img_gelap, "Gambar/red_gelap.jpeg", "Gambar/green_gelap.jpeg", "Gambar/blue_gelap.jpeg")

# fungsi untuk menampilkan photo Ori,R,G,B ke dalam 1 baris
def show_rgb(ori, red, green, blue):
    img = cv2.imread(ori)
    img1 = cv2.imread(red)
    img2 = cv2.imread(green)
    img3 = cv2.imread(blue)

    # fungsi yang mengembalikan tupel yang berisi gambar dan objek sumbu
    fig, axs = plt.subplots(1, 4, figsize=(20,15))

    axs[0].set_title("Original Photo")
    axs[0].imshow(img)
    axs[1].set_title("Channel R Photo")
    axs[1].imshow(img1)
    axs[2].set_title("Channel G Photo")
    axs[2].imshow(img2)
    axs[3].set_title("Channel B Photo")
    axs[3].imshow(img3)

    plt.show()

# fungsi menampilkan semua gambar asli dan r,g,b
def show_all_rgb():
    show_rgb("Gambar/terang.jpeg", "Gambar/red_terang.jpeg", "Gambar/green_terang.jpeg", "Gambar/blue_terang.jpeg")
    show_rgb("Gambar/sedang.jpeg", "Gambar/red_sedang.jpeg", "Gambar/green_sedang.jpeg", "Gambar/blue_sedang.jpeg")
    show_rgb("Gambar/gelap.jpeg", "Gambar/red_gelap.jpeg", "Gambar/green_gelap.jpeg", "Gambar/blue_gelap.jpeg")

# fungsi histogram channel R,G,B dengan berbagai bins
def histogram(image, bins, title, titleR, titleG, titleB):
    img = cv2.imread(image)
    r, g, b = cv2.split(img)

    fig, axs = plt.subplots(1, 4, figsize=(20,5))
    axs[0].set_title(title)
    axs[0].hist(img.ravel(), bins, [0,256], color='purple', alpha=0.5)
    axs[1].set_title(titleR)
    axs[1].hist(r.ravel(), bins, [0,256], color='red', alpha=0.5)
    axs[2].set_title(titleG)
    axs[2].hist(g.ravel(), bins, [0,256], color='green', alpha=0.5)
    axs[3].set_title(titleB)
    axs[3].hist(b.ravel(), bins, [0,256], color='blue', alpha=0.5)

# menampilkan fungsi histogram(image, bins, title) 256 bins
def histo_all():
    histogram("Gambar/terang.jpeg", 256, "Histogram Foto Terang (256 Bins)", "Channel R (256 Bins)", "Channel G (256 Bins)", "Channel B (256 Bins)")
    histogram("Gambar/sedang.jpeg", 256, "Histogram Foto Sedang (256 Bins)", "Channel R (256 Bins)", "Channel G (256 Bins)", "Channel B (256 Bins)")
    histogram("Gambar/gelap.jpeg", 256, "Histogram Foto Gelap (256 Bins)", "Channel R (256 Bins)", "Channel G (256 Bins)", "Channel B (256 Bins)")

# foto terang per-channel dan per-bins
def terang_bins():
    show_rgb("Gambar/terang.jpeg", "Gambar/red_terang.jpeg", "Gambar/green_terang.jpeg", "Gambar/blue_terang.jpeg")
    figure(0)
    histogram("Gambar/terang.jpeg", 4, "Histogram Foto Terang (4 Bins)", "Channel R (4 Bins)", "Channel G (4 Bins)", "Channel B (4 Bins)")
    figure(1) 
    histogram("Gambar/terang.jpeg", 8, "Histogram Foto Terang (8 Bins)", "Channel R (8 Bins)", "Channel G (8 Bins)", "Channel B (8 Bins)")
    figure(2)
    histogram("Gambar/terang.jpeg", 16, "Histogram Foto Terang (16 Bins)", "Channel R (16 Bins)", "Channel G (16 Bins)", "Channel B (16 Bins)")
    figure(3)
    histogram("Gambar/terang.jpeg", 32, "Histogram Foto Terang (32 Bins)", "Channel R (32 Bins)", "Channel G (32 Bins)", "Channel B (32 Bins)")
    figure(4)
    histogram("Gambar/terang.jpeg", 256, "Histogram Foto Terang (256 Bins)", "Channel R (256 Bins)", "Channel G (256 Bins)", "Channel B (256 Bins)")

# foto sedang per-channel dan per-bins
def sedang_bins():
    show_rgb("Gambar/sedang.jpeg", "Gambar/red_sedang.jpeg", "Gambar/green_sedang.jpeg", "Gambar/blue_sedang.jpeg")
    figure(0)
    histogram("Gambar/sedang.jpeg", 4, "Histogram Foto Sedang (4 Bins)", "Channel R (4 Bins)", "Channel G (4 Bins)", "Channel B (4 Bins)")
    figure(1) 
    histogram("Gambar/sedang.jpeg", 8, "Histogram Foto Sedang (8 Bins)", "Channel R (8 Bins)", "Channel G (8 Bins)", "Channel B (8 Bins)")
    figure(2)
    histogram("Gambar/sedang.jpeg", 16, "Histogram Foto Sedang (16 Bins)", "Channel R (16 Bins)", "Channel G (16 Bins)", "Channel B (16 Bins)")
    figure(3)
    histogram("Gambar/sedang.jpeg", 32, "Histogram Foto Sedang (32 Bins)", "Channel R (32 Bins)", "Channel G (32 Bins)", "Channel B (32 Bins)")
    figure(4)
    histogram("Gambar/sedang.jpeg", 256, "Histogram Foto Sedang (256 Bins)", "Channel R (256 Bins)", "Channel G (256 Bins)", "Channel B (256 Bins)")

# foto gelap per-channel dan per-bins
def gelap_bins():
    show_rgb("Gambar/gelap.jpeg", "Gambar/red_gelap.jpeg", "Gambar/green_gelap.jpeg", "Gambar/blue_gelap.jpeg")
    figure(0)
    histogram("Gambar/gelap.jpeg", 4, "Histogram Foto Gelap (4 Bins)", "Channel R (4 Bins)", "Channel G (4 Bins)", "Channel B (4 Bins)")
    figure(1) 
    histogram("Gambar/gelap.jpeg", 8, "Histogram Foto Gelap (8 Bins)", "Channel R (8 Bins)", "Channel G (8 Bins)", "Channel B (8 Bins)")
    figure(2)
    histogram("Gambar/gelap.jpeg", 16, "Histogram Foto Gelap (16 Bins)", "Channel R (16 Bins)", "Channel G (16 Bins)", "Channel B (16 Bins)")
    figure(3)
    histogram("Gambar/gelap.jpeg", 32, "Histogram Foto Gelap (32 Bins)", "Channel R (32 Bins)", "Channel G (32 Bins)", "Channel B (32 Bins)")
    figure(4)
    histogram("Gambar/gelap.jpeg", 256, "Histogram Foto Gelap (256 Bins)", "Channel R (256 Bins)", "Channel G (256 Bins)", "Channel B (256 Bins)")

def pilih_gambar():
    print('''
    1. Terang
    2. Sedang
    3. Gelap
    ''')

def menu():
    print('''
        Main Menu:
    1. Lihat Gambar Asli
    2. Lihat Gambar Channel R,G,B
    3. Lihat Histogram Gambar Asli 256 bins
    4. Lihat Histogram Gambar R,G,B (4,8,16,32,256 Bins)
    5. Keluar
    ''')

def main():
    loop = True
    while(loop):
        menu()
        ch_menu = input("Pilih: ")

        if ch_menu == '1':
            show_asli()
        elif ch_menu == '2':
            rgb_photo()
            show_all_rgb()
        elif ch_menu == '3':
            histo_all()
        elif ch_menu == '4':
            pilih_gambar()
            ch_gambar = input("Pilih: ")

            if ch_gambar == '1':
                terang_bins()
            elif ch_gambar == '2':
                sedang_bins()
            elif ch_gambar == '3':
                gelap_bins()
            else:
                print("Pilihan Tidak Tersedia")
                loop = False
        elif ch_menu == '5':
            exit(0)
        else:
            print("Pilihan Tidak Tersedia")
            loop = False

main()