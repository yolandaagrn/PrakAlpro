#Nama : Yolanda Anggraini
#Universitas Kristen Duta Wacana
#Materi : Struktur Control Percabangan
#Referensi soal : https://teamhannamy.blogspot.com/2021/02/17-contoh-soal-algoritma-percabangan

'''
input = jumlah total harga pembelian, jumlah barang yang dibeli
proses = percabangan if else
output = apakah pelanggan mendapatkan bonus atau tidak?

'''

total_harga_pembelian = int(input('Berapa jumlah total harga yang dikeluarkan? Rp. '))
jumlah_barang = int(input('Berapa jumlah barang yang dibeli? '))

if total_harga_pembelian >= 1000000 and jumlah_barang >= 5:
    print('Selamat anda mendapatkan bonus setrika')
elif total_harga_pembelian >= 500000 and jumlah_barang >= 3:
    print('Selamat anda mendapatkan bonus payung')
elif total_harga_pembelian >= 100000 and jumlah_barang >= 2:
    print('Selamat anda mendapatkan cangkir')
else:
    print('Anda tidak mendapatkan bonus apapun')