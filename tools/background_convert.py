import cv2

# membaca gambar
img = cv2.imread('nama_file_gambar.jpg')

# mengubah ke format HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# mengatur range warna yang akan diubah (contoh: hijau)
lower_green = (25, 52, 72)
upper_green = (102, 255, 255)

# menciptakan mask dengan range warna yang telah ditentukan
mask = cv2.inRange(hsv, lower_green, upper_green)

# mengubah warna yang terdeteksi oleh mask menjadi putih
img[mask > 0] = (255, 255, 255)

# menyimpan gambar yang telah diubah ke file baru
cv2.imwrite('nama_file_gambar_baru.jpg', img)
