#Nama : Yolanda Anggraini
#Universitas Kristen Duta Wacana
#Materi:Struktur Kontrol Perulangan
#tabel pembagian 50 bilangan
'''
input= bilangan pembagi dari user
proses= for i in range. membagi angka&pembagi
output=1-50 yang sudah dibagi dengan pembagi dan hasil bagi
'''
#1
bilangan = int(input('Mau pembagian berapa? '))
for i in range(0,50,1):
    pembagian = bilangan/(i+1)
    print(bilangan,'/',i+1,'=',pembagian)

#2
bilangan = int(input('Mau pembagian berapa? '))
for i in range(0,50,1):
    pembagian = (i+1)/bilangan
    print(i+1,'/',bilangan,'=',pembagian)