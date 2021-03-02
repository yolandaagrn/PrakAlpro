#Nama : Yolanda Anggraini
#Universitas Kristen Duta Wacana
#Materi : Modular Programming

'''
#Membuat kalkulator BMI

input = tinggi badan
prosesnya = (tinggi - 100) - ((15/100)*(tinggi-100))
output = berat ideal seharusnya
'''

print('='*25, 'KALKULATOR BMI', '='*25)

def berat_ideal(tinggi):
    ideal = (tinggi - 100) - ((15/100)*(tinggi-100))
    return ideal

tinggi = int(input('Masukkan tinggi badan anda saat ini: '))
print('Berat badan ideal anda seharusnya adalah ',berat_ideal(tinggi),'kg')

print('='*60)

''

'''
input = jumlah novel yang dibeli
prosesnya = jumlah novel * harga novel
output = total harga harus dibayar
'''

print('='*25,'KALKULATOR RESELER NOVEL','='*25)

def harga_bayar(barang):
    harga = 87000
    bayar = harga * barang
    return bayar
barang = int(input('Jumlah barang yang dibeli: '))
print('Total uang yang harus dikeuarkan untuk membayar adalah Rp.',harga_bayar(barang))

print('='*60)