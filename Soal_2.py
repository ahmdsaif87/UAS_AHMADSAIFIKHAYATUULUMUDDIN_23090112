import pandas as pd

nilai_mahasiswa = {
    'Mahasiswa 1' : [90,80],
    'Mahasiswa 2' : [50,60],
    'Mahasiswa 3' : [65,70],
}

df = pd.DataFrame(nilai_mahasiswa, index=['Algoritma dan Struktur Data 2', 'Matematika Numerik']).T

print('='*5,'Data Nilai Mahasiswa','='*5)
print(df)
print()


print('1. Tampilkan nilai rata-rata setiap mata kuliah')
print('2. Tampilkan nilai rata-rata setiap mahasiswa')
pilihan = input('Masukkan Pilihan: ')
while True:
    if pilihan == '1':
        df.mean()
    elif pilihan == '2':
        df.mean
