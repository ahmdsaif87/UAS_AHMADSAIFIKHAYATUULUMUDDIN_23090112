class Buah:
    def __init__(self, nama, warna, rasa):
        self.__nama = nama
        self.__warna = warna
        self.__rasa = rasa
        
    def set_nama(self, nama):
        self.__nama = nama
        
    def set_warna(self, warna):
        self.__warna = warna

    def set_rasa(self, rasa):
        self.__rasa = rasa
        
    def informasi(self):
        return f'Nama Buah : {self.__nama}\nWarna : {self.__warna}\nRasa : {self.__rasa}'  
        
class Mangga(Buah):
    def __init__(self, nama, warna, rasa, vitamin):
        Buah.__init__(self,nama, warna, rasa)
        self.__vitamin = vitamin
    
    def set_vitamin(self, vitamin):
        self.__vitamin = vitamin
    
    def information(self):
        return f'{self.informasi()}\nVitamin : {self.__vitamin}'
    