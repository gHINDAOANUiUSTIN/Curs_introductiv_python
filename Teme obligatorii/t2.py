# Ex. 1: Explică cu cuvintele tale în cadrul unui comentariu cum funcționează un if else.
""" O functie if else este caracterizata de faptul ca aceasta poate efectua operatii in functie de una sau mai multe
conditii stabilite.
Daca se indeplineste conditia if se va parcurge urmatoarea linie/secventa de cod si se va omite parcurgerea
liniei/secventei de cod else
Daca nu se indeplineste conditia if nu se va parcurge urmatoarea linie/secventa de cod si se va efectua else
"""

# Ex. 2: Verifică și afișează dacă x este număr natural sau nu.

x = float(input('Ex 2: Introduceti un numar: '))
if x.is_integer() == 1:
    if x >= 0:
        x = int(x)
        print(f'x = {x} este un numar natural')
    else:
        x = int(x)
        print(f'x = {x} este un numar intreg')
else:
    print(f'x = {x} este un numar real')


# Ex. 3: Verifică și afișează dacă x este număr pozitiv, negativ sau neutru.

x = int(input('Ex 3: Introduceti un numar intreg: '))
if x > 0:
    print(f'x = {x} este un numar pozitiv')
elif x < 0:
    print(f'x = {x} este un numar negativ')
else:
    print(f'x = {x} este nul')


# Ex. 4: Verifică și afișează dacă x este între -2 și 13

x = int(input('Ex 4: Introduceti un numar intreg: '))
if -2 < x < 13:
    print(f'x = {x} este cuprins in tervalul (-2,13)')
else:
    print(f'x = {x} nu este cuprins in tervalul (-2,13)')


# Ex. 5: Verifică și afișează dacă diferența dintre x și y este mai mică de 5.
x = int(input('Ex 5: Introduceti un numar intreg x: '))
y = int(input('Ex 5: Introduceti un numar intreg y: '))
if x-y < 5:
    print(f'Diferenta dintre numerele introduse x = {x} si y = {y} este mai mica de 5')
else:
    print(f'Diferenta dintre numerele introduse x = {x} si y = {y} este mai mare de 5')


# Ex. 6: Verifică dacă x NU este între 5 și 27 - a se folosi ‘not’.
x = int(input('Ex 6: Introduceti un numar intreg: '))
if x not in range(5, 27):
    print(f'x = {x} nu este cuprins in tervalul (5,27)')
else:
    print(f'x = {x} este cuprins in tervalul (5,27)')


# Ex. 7: x și y (int); Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai mare.
x = int(input('Ex 7: Introduceti un numar intreg x: '))
y = int(input('Ex 7: Introduceti un numar intreg y: '))
if x != y:
    if x > y:
        print(f'x = {x} este mai mare decat y = {y}')
    else:
        print(f'y = {y} este mai mare decat x = {x}')
else:
    print(f'x = y = {x}')


# Ex. 8: x, y, z - laturile unui triunghi; Afișează dacă triunghiul este isoscel, echilateral sau oarecare
x = int(input('Ex 8: Introduceti dimensiunea laturii x: '))
y = int(input('Ex 8: Introduceti dimensiunea laturii y: '))
z = int(input('Ex 8: Introduceti dimensiunea laturii z: '))
if x == y == z:
    print(f'Triunghiul format din laturile x = {x}, y = {y} si z = {z} este echilateral')
elif x == y or y == z or x == z:
    print(f'Triunghiul format din laturile x = {x}, y = {y} si z = {z} este isoscel')
else:
    print(f'Triunghiul format din laturile x = {x}, y = {y} si z = {z} este oarecare')


# Ex. 9: Citește o literă de la tastatură. Verifică și afișează dacă este vocală sau nu.
x = input('Ex 9: Introduceti o litera: ')
if x == 'a' or x == 'e' or x == 'i' == x == 'o' or x == 'u':
    print(f'Litera {x} este o vocala')
else:
    print(f'Litera {x} este o consoana')


# Ex. 10: Transformă și printează notele din sistem românesc în >
# Peste 9 => A
# Peste 8 => B
# Peste 7 => C
# Peste 6 => D
# Peste 4 => E
# 4 sau sub 4 => F

x = float(input('Ex 10: Introduceti o nota pentru conversie: '))
if x > 10 or x < 0:
    print(f'Nota introdusa nu este valida.')
else:
    if x >= 9:
        print(f'Echivalentul notei {x} este A')
    elif x >= 8:
        print(f'Echivalentul notei {x} este B')
    elif x >= 7:
        print(f'Echivalentul notei {x} este C')
    elif x >= 6:
        print(f'Echivalentul notei {x} este D')
    elif x > 4:
        print(f'Echivalentul notei {x} este E')
    else:
        print(f'Echivalentul notei {x} este F')
