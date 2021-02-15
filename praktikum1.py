#Nama : Yolanda Anggraini
#Universitas Kristen Duta Wacana

#survey beberapa mahasiswa dari beberapa ukm, terdapat ukm padus,basket,futsal,mapala,dan dance

'''
input: mahasiswa yang akan disurvey, mahasiswa yang ikut padus, ikut basket, ikut futsal, ikut mapala, dan ikut dance
proses: cek mahasiswa yang disurvey, cek mahasiswa padus, cek ikut basket, cek ikut futsal, cek mahasiswa ikut mapala, dan cek ikut dance
output: persentase dari mahasiswa ikut padus, ikut basket, ikut futsal, ikut mapala, dan ikut dance berdasarkan jumlah mahasiswa yang disurvey
'''
print('-'*20,'Survei Mahasiswa','-'*20)

mahasiswa_disurvey = int(input('Berapa mahasiswa yang disurvey: '))
padus = int(input('Berapa mahasiswa yang ikut padus: '))
basket = int(input('Berapa mahasiswa yang ikut basket: '))
futsal = int(input('Berapa mahasiswa yang ikut futsal: '))
mapala = int(input('Berapa mahasiswa yang ikut mapala: '))
dance = int(input('Berapa mahasiswa yang ikut dance: '))

persentase_padus = (padus/mahasiswa_disurvey)*100
persentase_basket = (basket/mahasiswa_disurvey)*100
persentase_futsal = (futsal/mahasiswa_disurvey)*100
persentase_mapala = (mapala/mahasiswa_disurvey)*100
persentase_dance = (dance/mahasiswa_disurvey)*100

print("Persentase mahasiswa yang mengikuti padus adalah", persentase_padus,"%")
print("Persentase mahasiswa yang mengikuti basket adalah", persentase_basket,"%")
print("persentase mahasiswa yang mengikuti futsal adalah", persentase_futsal,"%")
print("Persentase mahasiswa yang mengikuti mapala adalah", persentase_mapala,"%")
print("Persentase mahasiswa yang mengikuti dance adalah", persentase_dance,"%")