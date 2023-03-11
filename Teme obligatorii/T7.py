from abc import ABC, abstractmethod

#Clasa abstractă FormaGeometrica
class FormaGeometrica (ABC):

    # Conține un field PI=3.14
    PI = 3.14

    # Conține o metodă abstractă aria (opțional)
    @abstractmethod
    def aria(self):
        pass

    # Conține o metodă a clasei, descrie() - aceasta printează pe ecran ‘Cel mai probabil am colturi’
    @classmethod
    def descrie (cls):
        print("Cel mai probabil am colturi")


#Clasa Pătrat - moștenește FormaGeometrica
class Patrat (FormaGeometrica):

    # constructor pentru latură
    def __init__(self, latura):
        self.__latura = latura

    # Implementează metoda cerută de interfață (opțional, doar dacă ai ales să implementezi metoda abstractă aria)
    def aria(self):
        return self.__latura * self.__latura

    # latura este proprietate protected

    # Implementează getter, setter, deleter pentru latură
    @property
    def latura (self):
        return self.__latura

    @latura.getter
    def get_latura(self):
        print(f'Getter: latura este {self.__latura}')
        return self.__latura

    #latura.setter
    def set_latura(self, latura):
        print(f'Setter: Noua latura este {latura}')
        self.__latura = latura

    #latura.deleter
    def del_latura(self):
        print(f'Deleter: Am sters latura')
        self.__latura = None

#Clasa Cerc - moștenește FormaGeometrica
class Cerc(FormaGeometrica):

    # constructor pentru rază
    def __init__(self, raza):
        self.__raza = raza

    # raza este proprietate privată

    # Implementează getter, setter, deleter pentru rază
    @property
    def raza(self):
        return self.__raza

    @raza.getter
    def get_raza(self):
        print(f'Raza cercului este: {self.__raza}')
        return self.__raza

    #raza.setter
    def set_raza(self, raza):
        print(f'Noua valoarea a razei este: {raza}')
        self.__raza = raza

    #raza.deleter
    def del_raza(self):
        print(f'Am sters valoarea razei')
        self.__raza = None

    # Implementează metoda cerută de interfață - în calcul folosește field PI
    # mostenit din clasa părinte (opțional, doar dacă ai ales să implementezi metoda abstractă aria)
    def aria(self):
        aria_cercului = self.PI * self.__raza * self.__raza
        return aria_cercului

    # Definește o nouă metodă descrie - printează ‘Eu nu am colturi’
    def descrie(self):
        print(f'Eu nu am colturi')




#Creează un obiect de tip Patrat și joacă-te cu metodele lui
patrat = Patrat(4)
patrat.get_latura
patrat.set_latura(2)
patrat.del_latura()
patrat.get_latura

#Creează un obiect de tip Cerc și joacă-te cu metodele lui
cerc = Cerc(2)
cerc.get_raza
cerc.set_raza(4)
cerc.del_raza()
cerc.get_raza