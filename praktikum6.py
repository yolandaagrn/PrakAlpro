#Nama : Yolanda Anggraini
#Universitas Kristen Duta Wacana
#Materi:Percabangan dan perulangan komplex

'''
input=angka baris
proses=for i in range
output=pola kotak, siku dan segitiga
'''

angka = int(input('Masukkan angka: '))
for i in range(angka):
    for j in range(angka):
        print('*',end=" ")
    print()

angka = int(input('Masukkan angka: '))
for i in range(angka):
    for j in range(i,angka):
        print('*', end=" ")
    print()

angka = int(input('Masukkan angka: '))
for i in range(angka):
    for j in range(angka-i):
        print(" ", end=" ")
    for l in range(2*i):
        print("*", end=" ")
    print('*')