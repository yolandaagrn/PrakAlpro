#Nama = Yolanda Anggraini
#Materi Membaca dan Menulis File
#Universitas Kristen Duta Wacana
#mencari rumus dalam file kumpulan rumus bangun datar
#referensi : https://www.petanikode.com/python-file/

#membaca file
while True:
    file = open('rumus bangun.txt','r')
    dicari = input('Rumus luas bangun yang dibutuhkan: ')
    for line in file:
        if line.startswith(dicari):
            print('Rumus: ',line)
    lagi = input('Cari lagi (y/t)? ')
    if lagi == 'y':
        for line in file:
            if line.startswith(dicari):
                print('Rumus: ',line)
    else:
        break
print()

#menulis file
file = open('biodata.txt','w')
nama = input('Nama: ')
ttl = input('TTL: ')
alamat = input('Alamat: ')
telp = input('No Hp: ')

teks = 'Nama: {} \nTTL: {} \nAlamat: {} \nNo Hp: {}'.format(nama,ttl,alamat,telp)
file.write(teks)
file.close()