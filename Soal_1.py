mahasiswa = []

def tambah():
    nim_mahasiswa = input("Masukkan NIM: ")
    nama_mahasiswa = input("Masukkan Nama: ")
    tampung_mahasiswa = {'NIM': nim_mahasiswa, 'Nama': nama_mahasiswa}
    mahasiswa.append(tampung_mahasiswa)
    print(f'{nama_mahasiswa} telah ditambahkan ke dalam mahasiswa')

def tampilkan():
    if not mahasiswa:
        print("Belum ada mahasiswa yang tersimpan.")
    else:
        print("Daftar mahasiswa:")
        for i in mahasiswa:
            print(f"NIM: {i['NIM']}, Nama: {i['Nama']}")

def tampilan():
    while True:
           tambah()
           pilihan = input('Ingin Tambah Lagi? ')
           if pilihan == 'Ya':
               tambah()
           elif pilihan == 'Tidak':
               tampilkan()
               break

tampilan()