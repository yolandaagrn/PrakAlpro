import re

#Nama : Yolanda Anggraini
#NIM : 71200649
#Universitas Kristen Duta Wacana
#Materi : RegEx

import re
teks = 'Lala = 085722683228, Ghiffa = 0897789098234, Ozi = 089522789555'

for angka in teks:
    nomor = re.findall('\d{12}', teks)
print('No yang ditemukan: ', nomor)