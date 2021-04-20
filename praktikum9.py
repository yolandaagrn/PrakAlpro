#Nama = Yolanda Anggraini
#Universitas Kristen Duta Wacana
#Materi List
#Soal: menghitung macam, jumlah, dan harga total barang belanja

barang = ['odol', 'sabun','mie','kopi']
banyak = ['1','4','5','5']
harga = ['7000','3000','2700','2000']

def belanjaan(barang):
    hitung = len(barang)
    return hitung
jenis_barang = len(barang)

#list
print('List belanja: ',barang)

#macam barang
print('Ada',jenis_barang,'macam barang yang harus dibeli')

#jumlah barang
total = int(banyak[0]) + int(banyak[1]) + int(banyak[2]) + int(banyak[3])
print('Barang keseluruhan ada',total,'barang')

#total harga
harganya = int(banyak[0])*int(harga[0]) + int(banyak[1])*int(harga[1]) + int(banyak[2])*int(harga[2]) + int(banyak[3])*int(harga[3])
print('Harga total belanja adalah Rp.',harganya)
