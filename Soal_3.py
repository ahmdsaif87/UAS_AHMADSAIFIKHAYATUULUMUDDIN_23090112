antrian = []

def enqueue(item):
    antrian.append(item)

def dequeue():
    antrian.pop(0)

def lihat_antrian():
    if len(antrian) == 0:
        print('Antrian Kosong')
    else:
        for index,value in enumerate(antrian):
            print(f'{index}: {value}')

def tampilan():
    while True:
        print('Pilihan')
        print('1. Tambah Antrian')
        print('2. Hapus Antrian')
        print('3. Lihat Antrian')
        print('4. Keluar')
        main = input('Masukkan Pilihan:')
        if main == '1':
            item = input('Masukkan nama pelanggan: ')
            enqueue(item)
            print('=' * 20)
        elif main == '2':
            dequeue()
        elif main == '3':
            print('List Antrian:')
            lihat_antrian()
            print('=' * 20)
        else:
            break
            
tampilan()