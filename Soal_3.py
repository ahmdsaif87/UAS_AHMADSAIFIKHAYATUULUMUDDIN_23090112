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
