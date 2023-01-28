from math import pi
# Ex1:Funcție care să calculeze și să returneze suma a două numere

def suma(a, b):
    return a + b


print(f'Ex1: {suma(3,4)}')


# Ex2: Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar

def par_impar (a):
    if a % 2 == 0:
        return True
    else:
        return False


print(f'Ex2: {par_impar(5)}')


# Ex3: Funcție care returnează numărul total de caractere din numele tău complet.
# (nume, prenume, nume_mijlociu)

def nr_caractere (nume, prenume1, prenume2):
    return len(nume) + len(prenume1) + len(prenume2)


print(f'Ex3: {nr_caractere("Gheorghe", "Matei", "Corvin")}')


# Ex4: Funcție care returnează aria dreptunghiului

def arie_dreptunghi (l1, l2):
    return l1 * l2


print(f'Ex4: {arie_dreptunghi(10,5)}')


# Ex5: Funcție care returnează aria cercului

def arie_cerc (r):
    return pi ** r


print(f'Ex5: {arie_cerc(5)}')


# Ex6: Funcție care returnează True dacă un caracter x se găsește într-un string dat și Talse dacă nu găsește.

def finder (c, sir):
    if c in sir:
        return True
    else:
        return False


print(f'Ex6: {finder("m", "mama are mere")}')


# Ex7: Funcție fără return, primește un string și printează pe ecran:
# ● Nr de caractere lower case este x
# ● Nr de caractere upper case exte y

def nr_carctere (sirr):
    up = low = 0
    for i in range (0, len(sirr)):
        if sirr[i].isalpha():
            if sirr[i].isupper():
                up += 1
            else:
                low += 1
        else:
            continue
    print(f'Ex7: Numarul de litere lower este {low}, iar numarul de litere upper este {up}')


nr_carctere(sirr=input("Ex7: Introduceti un sir de caractere: "))


# Ex8: Funcție care primește o LISTA de numere și returnează o LISTA doar cu numerele pozitive

nr_items = int(input("Ex8: Inainte de a introduce o lista de numere, introduceti dimensiunea acesteia: "))
lista_numere = []
for i in range(1, nr_items+1):
    lista_numere.append(int(input(f"Ex8: Introduceti elementul {i} din lista si apasati enter: ")))


def lista_poz(lista_numere):
    lista_nr_poz = []
    for n in range(0, nr_items):
        if lista_numere[n] >= 0:
            lista_nr_poz.append(lista_numere[n])
    return lista_nr_poz


print(f"Ex8: Lista obtinuta din numerele introduse care sunt pozitive: {lista_poz(lista_numere)}")


# Ex9: Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA


def compare():
    x = int(input("Ex9: Introduceti primul numar pentru comparare: "))
    y = int(input("Ex9: Introduceti al doilea numar pentru comparare: "))
    if x > y:
        print(f'Ex9: Primul numar {x} este mai mare decat al doilea numar {y}')
        # ● Primul număr x este mai mare decat al doilea nr y
    elif x < y:
        print(f'Ex9: Al doilea numar {y} este mai mare decat primul numar {x}')
        # ● Al doilea nr y este mai mare decat primul nr x
    else:
        print("Ex9: Numerele sunt egale")
        # ● Numerele sunt egale.


compare()


# Ex10: Funcție care primește un număr și un set de numere.
nr_numere = int(input("Ex10: Inainte de a introduce un set de numere, introduceti dimensiunea acestuia = "))
set_numere = set()
for i in range(1, nr_numere+1):
    set_numere.add(int(input(f"Ex10: Introduceti elementul {i} din lista si apasati enter: ")))


def set_add ():
    nr_add = int(input("Ex10: Introduceti un numar pe care doriti sa-l adaugati la set: "))
    if nr_add not in set_numere:
        set_numere.add(nr_add)
        # ● Printeaza ‘am adaugat numărul nou în set’ + returnează True
        print("Ex10: Am adaugat numărul nou în set.")
        print(f'Ex10: Noul set de numere este: {set_numere}')
        return True
    else:
        # ● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ + returnează False
        print("Ex10: Nu am adaugat numărul în set. Acesta există deja.")
        return False


set_add()
