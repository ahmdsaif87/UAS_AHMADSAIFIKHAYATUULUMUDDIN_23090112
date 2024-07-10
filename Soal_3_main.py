import Soal_3

while True:
        print('Pilihan')
        print('1. Tambah Antrian')
        print('2. Hapus Antrian')
        print('3. Lihat Antrian')
        print('4. Keluar')
        main = input('Masukkan Pilihan:')
        if main == '1':
            item = input('Masukkan nama pelanggan: ')
            Soal_3.enqueue(item)
            print('=' * 20)
        elif main == '2':
            Soal_3.dequeue()
        elif main == '3':
            print('List Antrian:')
            Soal_3.lihat_antrian()
            print('=' * 20)
        else:
            break