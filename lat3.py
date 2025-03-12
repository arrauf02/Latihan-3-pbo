from abc import ABC, abstractmethod
class mahasiswa:
    def __init__(self, nama , nim, ketawa):
        self._nama = nama
        self._nim = nim
        self._ketawa = ketawa
    
    @property
    def nama(self):
        return self._nama
    
    @property
    def nim(self):
        return self._nim
    
    @abstractmethod
    def suara_ketawa(self):
        pass

def cara_ketawa(mahasiswa):
    print(mahasiswa.suara_ketawa())

class danang :
    def suara_ketawa(self):
        return "ang ang ang ang"
    
class garis :
    def suara_ketawa(self):
        return "hahahaha"
        

cara_ketawa(danang())
cara_ketawa(garis())
        