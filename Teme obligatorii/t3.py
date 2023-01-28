'''
Pentru toate exercițiile se va folosi noțiunea de if în rezolvare.
Indirect vei exersa și operatorii în cadrul condițiilor ramurilor din if.
X poate fi inițializat direct în cod sau citit de la tastatură, după preferințe.
X este un int.

Ex1: Declară o listă note_muzicale în care să pui do re mi etc până la do
● Afișeaz-o
● Inversează ordinea folosind slicing și suprascrie această listă.
● Printează varianta actuală (inversată).
● Pe această listă aplică o metodă care bănuiești că face același lucru,
adică să îi inverseze ordinea. Nu trebuie să o suprascrii în acest caz,
deoarece metoda face asta automat.
● Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta
inițială.
Concluzii: slicing e temporar, dacă vrei să păstrezi noua variantă va trebui să
suprascrii lista sau să o salvezi într-o listă nouă. Metoda găsită de tine face
suprascrierea automat și permanentizează aceste modificări. Ambele variante
își găsesc utilitatea în funcție de ce ne dorim în acel moment.
'''

# Ex1:
note_muzicale = ["do", "re", "mi", "fa", "sol", "la", "si", "do"]
print(note_muzicale)
note_muzicale = note_muzicale[::-1]
print(note_muzicale)
note_muzicale.reverse()
print(note_muzicale)

# Ex2: De câte ori apare ‘do’?
print(note_muzicale.count("do"))


# Ex3: Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
# Găsește 2 variante să le unești într-o singură listă.
list1 = [3, 1, 0, 2]
print(list1)
list2 = [6, 5, 4]
print(list2)
lists = list1 + list2
print (lists)
list1.extend(list2)
print(list1)

# Ex4:
# ● Sortează și afișază lista generată la exercițiul anterior.
# ● Sortează numărul 0 folosind o funcție.
# ● Afișaza iar lista.
list1.sort()
print(lists)


# Ex5: Folosind un if verifică lista generată la exercițiul 3 și afișază:
# ● Lista este goală.
# ● Lista nu este goală.
if len(lists) == 0:
    print("Lista este goala")
else:
    print("Lista nu este goala")
# Ex6: Folosește o funcție care să șteargă lista de la exercițiul 3.
lists.clear()

# Ex7: Copy paste la exercițiul 5. Verifică încă o dată.
#Acum ar trebui să se afișeze că lista e goală.
if len(lists) == 0:
    print("Lista este goala")
else:
    print("Lista nu este goala")

# Ex8: Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# Folosește o funcție că să afișezi Elevii (cheile)
dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
print(dict1.keys())
print ([key for key in dict1.keys()])
# Ex9: Printează cei 3 elevi și notele lor
# Ex: ‘Ana a luat nota {x}’
# Doar nota o vei lua folosindu-te de cheie
print(f"{[key for key in dict1.keys()][0]} a luat nota {dict1['Ana']}")
print(f"{[key for key in dict1.keys()][1]} a luat nota {dict1['Gigel']}")
print(f"{[key for key in dict1.keys()][2]} a luat nota {dict1['Dorel']}")

# Ex10: Dorel a făcut contestație și a primit 6
# ● Modifică nota lui Dorel în 6
# ● Printează nota după modificare
dict1['Dorel'] = 6
print (dict1['Dorel'])

# Ex11: Gigel se transferă din clasă
# ● Căuta o funcție care să îl șteargă
# ● Vine un coleg nou. Adaugă Ionică, cu nota 9
# ● Printează noii elevi
dict1.__delitem__('Gigel')
dict1['Ionica'] = 9
print (dict1)

# Ex12: Set
zile_sapt = {'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
#● Adaugă în zilele_sapt ‘luni’
#● Afișeaza zile_sapt
zile_sapt.add('luni')
print(zile_sapt)

# Ex13: Folosește un if și verifică dacă:
# ● Weekend este un subset al zilelor din săptămânii.
# ● Weekend nu este un subset al zilelor din săptămânii.
if weekend.issubset(zile_sapt):
    print("Weekend este un subset al zilelor săptămânii.")
else:
    print("Weekend nu este un subset al zilelor săptămânii.")

# Ex14: Afișează diferențele dintre aceste 2 seturi.
print(zile_sapt - weekend)

# Ex15: Afișază intersecția elementelor din aceste 2 seturi.
print(zile_sapt.intersection(weekend))
