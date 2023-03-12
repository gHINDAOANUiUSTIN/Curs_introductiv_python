#1. Ne imaginam o echipa de fotbal in timpul meciului. Sunt permise maxim 3 schimbari.
#- Declara o lista cu 5 jucatori: lista_jucatori_teren
lista_jucatori_teren = ['Alexe Radu', 'Petrescu Andrei', 'Doru Dinu', 'Rosu Cristi', 'Mihai Denis']
#- Declara o lista cu 5 jucatori de rezerva: lista_jucatori_rezerva
lista_jucatori_rezerva = ['Savu Alex', 'Pavel Petru', 'Albu Matei', 'Gelu Marin', 'Dica George']
#- Declara o lista goala cu jucatori scosi din teren: lista_jucatori_scosi
lista_jucatori_scosi = []
#- Schimbari_efectuate = joaca-te cu valori diferite ca sa vezi cum trec datele prin cod
schimbari_efectuate = 0
#- SCHIMBARI_MAX va fi o constanta cu valoarea 3
schimbari_max = 3
#Daca Jucatorul x e in teren si mai avem schimbari la dispozitie atunci:
if 'Alexe Radu' in lista_jucatori_teren and schimbari_efectuate<schimbari_max:
    #- Efectuam schimbarea daca jucatorul e in lista de rezerve si nu exista in jucatorii de pe teren
    if 'Savu Alex' in lista_jucatori_rezerva and 'Savu Alex' not in lista_jucatori_teren:
        #- Stergem jucatorul scos din lista de teren si il adaugam in lista de jucatori scosi
        #- Adaugam jucatorul intrat in lista de jucatori de pe teren si il scoatem din lista de jucatori de rezerva
        lista_jucatori_scosi.extend([lista_jucatori_teren[0]])
        lista_jucatori_teren[0] = lista_jucatori_rezerva[0]
        del lista_jucatori_rezerva[0]
        schimbari_efectuate = 1
        #- Afisam pe ecran: a intrat x, a iesit y. Mai aveti z schimbari (inlocuiti x, y si z cu numele variabilelor voastre)
        print (f"A intrat {lista_jucatori_teren[0]}, a iesit {lista_jucatori_scosi[0]}. Mai aveti {schimbari_max - schimbari_efectuate} schimbari")
#Daca jucatorul pe care vrem sa il schimbam nu e in teren:
if 'Albu Matei' not in lista_jucatori_teren:
    #- Afisati ‘nu se poate efectua schimbarea deoarece jucatorul x nu e in teren’
    print(f"Nu se poate efectua schimbarea deoarece jucatorul {lista_jucatori_rezerva[1]} nu este in teren")
    #Altfel, afisati ecran: ‘mai aveti z schimbari’
    print(f'Mai aveti {schimbari_max-schimbari_efectuate} schimbari.')

print(f'Lista jucatori teren: {lista_jucatori_teren},\n'
      f'Lista jucatori rezerva: {lista_jucatori_rezerva},\n'
      f'Lista jucatori scosi: {lista_jucatori_scosi}.')