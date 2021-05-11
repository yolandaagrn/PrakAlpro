#Nama = Yolanda Anggraini
#NIM = 71200649
#Universitas Kristen Duta Wacana
#Materi: SET (Program menghapus data)

menu = 0
while menu == 0:
    print('Daftar Nama')
    print('1. Cek data \n2. Hapus data \n3. Exit')
    pilih = int(input('Masukkan pilihan: '))

    mhs1 = {'Fawwaz', 2150001, 'Kedoteran'}
    mhs2 = {'Ozi', 7150002, 'Informatika'}
    mhs3 = {'Bram', 4120003, 'Akuntansi'}

    if pilih == 1:
        print(mhs1,mhs2,mhs3)

    elif pilih == 2:
        hapus = input('Masukkan nama dari data yang akan dihapus: ')
        nama = set(hapus)
        if hapus == 'fawwaz':
            hilang = nama.pop()
            print(mhs2,mhs3)
        elif hapus == 'ozi':
            hilang = nama.pop()
            print(mhs1,mhs3)
        elif hapus == 'bram':
            hilang = nama.pop()
            print(mhs1,mhs2)
    else:
        exit()