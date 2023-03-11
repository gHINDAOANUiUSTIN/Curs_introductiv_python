# Ex 1: Clasa Cerc:

class Cerc():

    # Atribute: raza, culoare
    def __init__(self, raza, culoare):
        # Constructor pentru ambele atribute
        self.raza = raza
        self.culoare = culoare
        self.PI = 3.14

    # Metode:
    # ● descrie_cerc() - va PRINTA culoarea și raza
    def descriere_cerc(self):
        print(f'Culoarea cercului este {self.culoare}, iar raza este {self.raza}')

    # ● aria() - va RETURNA aria
    def aria(self):
        return self.PI * self.raza ** 2

    # ● diametru()
    def diametru(self):
        return self.raza * 2

    # ● circumferinta()
    def circumferinta(self):
        return self.raza * self.PI * 2


c1 = Cerc(2, 'rosu')
c1.descriere_cerc()
print(c1.aria())
print(c1.diametru())
print(c1.circumferinta())


# Ex 2: Clasa Dreptunghi:

class Dreptunghi():

    # Atribute: lungime, latime, culoare
    def __init__(self, lungime, latime, culoare):
        # Constructor pentru ambele atribute
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    # Metode:
    # ● descrie()
    def descrie(self):
        print(f'Lungimea dreptunghiului este {self.lungime}')
        print(f'Latimea dreptunghiului este {self.latime}')
        print(f'Culoarea dreptunghiului este {self.culoare}')

    # ● aria()
    def aria(self):
        return self.lungime * self.latime

    # ● perimetrul()
    def perimetrul(self):
        return (self.lungime + self.latime) * 2

    # ● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
    # Ea va lua ca și parametru o nouă culoare și va suprascrie atributul
    def schimba_culoarea(self, noua_culoare):
        self.culoare = noua_culoare


d1 = Dreptunghi(6, 3, 'albastru')
d1.descrie()
print(d1.aria())
print(d1.perimetrul())
# self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei
# descrie()
d1.schimba_culoarea('rosu')
d1.descrie()


# Ex 3: Clasa Angajat

class Angajat():
    # Atribute: nume, prenume, salariu
    def __init__(self, nume, prenume, salariu):
        # Constructor pt toate atributele
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu




    # Metode:
    # ● descrie()
    def descrie(self):
        print(f"Numele angajatului este {self.nume}")
        print(f"Prenumele angajatului este {self.prenume}")
        print(f"Salariul angajatului este {self.salariu}")

    # ● nume_complet()
    def nume_complet(self):
        return self.nume + ' ' + self.prenume

    # ● salariu_lunar()
    def salariu_lunar(self):
        return self.salariu

    # ● salariu_anual()
    def salariu_anual(self):
        return self.salariu * 12

    # ● marire_salariu(procent)
    def marire_salariu(self, procent):
        self.procent = procent
        self.salariu = self.salariu + self.salariu * self.procent/100
        return self.salariu


a1 = Angajat('Doru', 'Marcel', 5000)
a1.descrie()
print(a1.nume_complet())
print(a1.salariu_lunar())
print(a1.salariu_anual())
print(a1.marire_salariu(30))


# Ex 4: Clasa Cont

class Cont():
    # Atribute: iban, titular_cont, sold
    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold
        # Constructor pentru toate atributele

    # Metode:
    # ● afisare_sold() - Titularul x are în contul y suma de n lei
    def afisare_sold(self):
        print(f'Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei.')

    # ● debitare_cont(suma)
    def debitare_cont(self, suma):
        self.suma = suma
        self.sold -= suma


    # ● creditare_cont(suma)
    def creditare_cont(self, suma):
        self.suma = suma
        self.sold += suma



cont1 = Cont('RO123BTRL123452', 'Udrea Elena', 5000000)
cont1.afisare_sold()
cont1.debitare_cont(10000000)
print(f'Dupa inapoierea banilor furati, soldul devine {cont1.sold} lei')
cont1.creditare_cont(4900000)
print(f'Dupa primirea unui ajutor financiar din partea unui prieten, soldul devine {cont1.sold} lei')
